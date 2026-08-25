#!/usr/bin/env python3
"""Google Workspace bridge for the Daily UI design challenge."""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import shutil
import sys
from datetime import datetime
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from bs4 import BeautifulSoup
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / "automation_config.json"
STATE_PATH = ROOT / "state.json"
TOKEN_PATH = ROOT / "token.json"
CREDENTIALS_PATH = ROOT / "credentials.json"
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/spreadsheets",
]
HEADERS = [
    "Day",
    "Challenge",
    "Prompt",
    "Email Date",
    "Gmail Message ID",
    "Status",
    "Reviewer Remarks",
    "Implementation Notes",
    "GitHub URL",
    "Drive URL",
    "Last Run IST",
    "Attempt Count",
    "Error",
]


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def config() -> dict[str, Any]:
    return load_json(CONFIG_PATH, {})


def credentials_file() -> Path:
    if CREDENTIALS_PATH.exists():
        return CREDENTIALS_PATH
    matches = sorted(ROOT.glob("client_secret_*.json"))
    if len(matches) == 1:
        return matches[0]
    raise FileNotFoundError(
        f"OAuth file not found. Save it as {CREDENTIALS_PATH} (or keep exactly one client_secret_*.json)."
    )


def get_credentials(interactive: bool = True) -> Credentials:
    creds: Any = None
    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    if not creds or not creds.valid:
        if not interactive:
            raise RuntimeError("Google OAuth token is missing or invalid; run bootstrap interactively.")
        flow = InstalledAppFlow.from_client_secrets_file(str(credentials_file()), SCOPES)
        creds = flow.run_local_server(port=0, open_browser=True)
    TOKEN_PATH.write_text(creds.to_json(), encoding="utf-8")
    os.chmod(TOKEN_PATH, 0o600)
    return creds


def services(interactive: bool = True):
    creds = get_credentials(interactive=interactive)
    return (
        build("gmail", "v1", credentials=creds, cache_discovery=False),
        build("drive", "v3", credentials=creds, cache_discovery=False),
        build("sheets", "v4", credentials=creds, cache_discovery=False),
    )


def decode_data(value: str) -> str:
    padded = value + "=" * (-len(value) % 4)
    return base64.urlsafe_b64decode(padded.encode()).decode("utf-8", errors="replace")


def extract_message_body(payload: dict[str, Any]) -> str:
    candidates: list[tuple[str, str]] = []

    def walk(part: dict[str, Any]) -> None:
        data = part.get("body", {}).get("data")
        mime = part.get("mimeType", "")
        if data and mime in {"text/plain", "text/html"}:
            candidates.append((mime, decode_data(data)))
        for child in part.get("parts", []) or []:
            walk(child)

    walk(payload)
    if not candidates:
        return ""
    plain = next((body for mime, body in candidates if mime == "text/plain"), None)
    if plain is not None:
        return re.sub(r"\n{3,}", "\n\n", plain).strip()
    soup = BeautifulSoup(candidates[0][1], "html.parser")
    return re.sub(r"\n{3,}", "\n\n", soup.get_text("\n", strip=True)).strip()


def extract_day(text: str) -> int | None:
    patterns = [
        r"(?i)daily\s*ui\s*#?\s*0*(\d{1,3})\b",
        r"(?i)(?:day|challenge)\s*#?\s*0*(\d{1,3})\b",
        r"#\s*0*(\d{1,3})\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            day = int(match.group(1))
            if 1 <= day <= 100:
                return day
    return None


def challenge_title(subject: str, day: int) -> str:
    cleaned = re.sub(r"(?i)daily\s*ui\s*#?\s*0*%d" % day, "", subject)
    cleaned = re.sub(r"^[\s|:—–-]+|[\s|:—–-]+$", "", cleaned).strip()
    return cleaned or f"Daily UI Challenge {day:03d}"


def extract_prompt(body: str) -> tuple[str | None, str]:
    """Extract the challenge title and concise instructions from newsletter text."""
    normalized = body.replace("\r\n", "\n").replace("\r", "\n")
    titled = re.search(r"(?is)\*Prompt:\s*(.*?)\*\s*(.*?)(?=\n\s*Share your design|\n\s*\[Image item\])", normalized)
    if titled:
        title = re.sub(r"\s+", " ", titled.group(1)).strip()
        instructions = re.sub(r"\n{3,}", "\n\n", titled.group(2)).strip()
        return title, f"Prompt: {title}\n\n{instructions}".strip()
    return None, normalized[:45000].strip()


def sanitize_name(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-")
    return re.sub(r"-+", "-", value)


def now_ist() -> str:
    return datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S IST")


def row_needs_work(row: dict[str, str]) -> bool:
    status = row.get("Status", "").strip().lower()
    remarks = row.get("Reviewer Remarks", "").strip()
    if status in {"new", "changes requested", "failed"}:
        return True
    return status == "pending review" and bool(remarks)


def ensure_resources(drive, sheets) -> dict[str, str]:
    state = load_json(STATE_PATH, {})
    cfg = config()
    folder_id = state.get("drive_folder_id")
    if not folder_id:
        name = cfg.get("drive_folder_name", "100 Days Design Challenge")
        escaped = name.replace("'", "\\'")
        result = drive.files().list(
            q=f"name='{escaped}' and mimeType='application/vnd.google-apps.folder' and trashed=false",
            fields="files(id,name)",
            spaces="drive",
        ).execute()
        files = result.get("files", [])
        if files:
            folder_id = files[0]["id"]
        else:
            folder_id = drive.files().create(
                body={"name": name, "mimeType": "application/vnd.google-apps.folder"},
                fields="id",
            ).execute()["id"]
        state["drive_folder_id"] = folder_id

    spreadsheet_id = state.get("spreadsheet_id")
    if not spreadsheet_id:
        title = cfg.get("spreadsheet_name", "100 Days Design Challenge - Review Board")
        created = sheets.spreadsheets().create(
            body={"properties": {"title": title}, "sheets": [{"properties": {"title": cfg.get("review_tab", "Challenges")}}]},
            fields="spreadsheetId",
        ).execute()
        spreadsheet_id = created["spreadsheetId"]
        drive.files().update(
            fileId=spreadsheet_id,
            addParents=folder_id,
            fields="id,parents",
        ).execute()
        state["spreadsheet_id"] = spreadsheet_id
        tab = cfg.get("review_tab", "Challenges")
        sheets.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=f"'{tab}'!A1:M1",
            valueInputOption="RAW",
            body={"values": [HEADERS]},
        ).execute()
        sheet_meta = sheets.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
        sheet_id = sheet_meta["sheets"][0]["properties"]["sheetId"]
        sheets.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body={
                "requests": [
                    {"updateSheetProperties": {"properties": {"sheetId": sheet_id, "gridProperties": {"frozenRowCount": 1}}, "fields": "gridProperties.frozenRowCount"}},
                    {"setDataValidation": {"range": {"sheetId": sheet_id, "startRowIndex": 1, "startColumnIndex": 5, "endColumnIndex": 6}, "rule": {"condition": {"type": "ONE_OF_LIST", "values": [{"userEnteredValue": x} for x in ["New", "In Progress", "Pending Review", "Changes Requested", "Approved", "Failed"]]}, "strict": True, "showCustomUi": True}}},
                ]
            },
        ).execute()
    save_json(STATE_PATH, state)
    return state


def read_rows(sheets, spreadsheet_id: str) -> list[dict[str, str]]:
    tab = config().get("review_tab", "Challenges")
    values = sheets.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=f"'{tab}'!A:M"
    ).execute().get("values", [])
    if not values:
        return []
    headers = values[0]
    rows = []
    for index, values_row in enumerate(values[1:], start=2):
        padded = values_row + [""] * (len(headers) - len(values_row))
        row = dict(zip(headers, padded))
        row["_row_number"] = str(index)
        rows.append(row)
    return rows


def sync_messages(gmail, sheets, state: dict[str, str]) -> dict[str, int]:
    query = config().get("gmail_query", "subject:\"Daily UI\"")
    message_ids: list[str] = []
    page_token = None
    while True:
        result = gmail.users().messages().list(
            userId="me", q=query, maxResults=100, pageToken=page_token
        ).execute()
        message_ids.extend(item["id"] for item in result.get("messages", []))
        page_token = result.get("nextPageToken")
        if not page_token:
            break
    existing_rows = read_rows(sheets, state["spreadsheet_id"])
    existing = {row.get("Gmail Message ID"): row for row in existing_rows}
    new_rows: list[list[Any]] = []
    skipped = 0
    updated = 0
    for message_id in reversed(message_ids):
        existing_row = existing.get(message_id)
        if existing_row and not existing_row.get("Challenge", "").startswith("Challenge #"):
            continue
        message = gmail.users().messages().get(userId="me", id=message_id, format="full").execute()
        headers = {h["name"].lower(): h["value"] for h in message.get("payload", {}).get("headers", [])}
        subject = headers.get("subject", "Daily UI")
        body = extract_message_body(message.get("payload", {}))
        day = extract_day(subject) or extract_day(body[:3000])
        if day is None:
            skipped += 1
            continue
        prompt_title, concise_prompt = extract_prompt(body)
        title = prompt_title or challenge_title(subject, day)
        if existing_row:
            update_row(sheets, state, existing_row, **{"Challenge": title, "Prompt": concise_prompt})
            updated += 1
            continue
        date_text = headers.get("date", "")
        try:
            email_date = parsedate_to_datetime(date_text).isoformat()
        except (TypeError, ValueError):
            email_date = date_text
        new_rows.append([
            day,
            title,
            concise_prompt,
            email_date,
            message_id,
            "New",
            "",
            "",
            "",
            "",
            now_ist(),
            0,
            "",
        ])
    if new_rows:
        tab = config().get("review_tab", "Challenges")
        sheets.spreadsheets().values().append(
            spreadsheetId=state["spreadsheet_id"],
            range=f"'{tab}'!A:M",
            valueInputOption="RAW",
            insertDataOption="INSERT_ROWS",
            body={"values": new_rows},
        ).execute()
    return {"matched": len(message_ids), "added": len(new_rows), "updated": updated, "skipped_without_day": skipped}


def find_row(sheets, state: dict[str, str], message_id: str) -> dict[str, str]:
    for row in read_rows(sheets, state["spreadsheet_id"]):
        if row.get("Gmail Message ID") == message_id:
            return row
    raise KeyError(f"No sheet row found for Gmail message {message_id}")


def update_row(sheets, state: dict[str, str], row: dict[str, str], **fields: Any) -> None:
    merged = {header: row.get(header, "") for header in HEADERS}
    for key, value in fields.items():
        if key not in HEADERS:
            raise KeyError(f"Unknown sheet field: {key}")
        merged[key] = value
    row_number = int(row["_row_number"])
    tab = config().get("review_tab", "Challenges")
    sheets.spreadsheets().values().update(
        spreadsheetId=state["spreadsheet_id"],
        range=f"'{tab}'!A{row_number}:M{row_number}",
        valueInputOption="RAW",
        body={"values": [[merged[h] for h in HEADERS]]},
    ).execute()


def upload_artifact(drive, state: dict[str, str], row: dict[str, str], artifact_dir: Path) -> str:
    if not artifact_dir.is_dir():
        raise FileNotFoundError(f"Artifact directory not found: {artifact_dir}")
    build_dir = ROOT / ".build"
    build_dir.mkdir(exist_ok=True)
    day = int(row["Day"])
    bundle_base = build_dir / f"day-{day:03d}"
    zip_path = Path(shutil.make_archive(str(bundle_base), "zip", root_dir=artifact_dir))
    message_id = row["Gmail Message ID"]
    escaped = message_id.replace("'", "\\'")
    query = f"appProperties has {{ key='gmailMessageId' and value='{escaped}' }} and trashed=false"
    existing = drive.files().list(q=query, fields="files(id,name)").execute().get("files", [])
    media = MediaFileUpload(str(zip_path), mimetype="application/zip", resumable=True)
    metadata = {
        "name": f"Day-{day:03d}-{sanitize_name(row['Challenge'])}.zip",
        "appProperties": {"gmailMessageId": message_id, "day": str(day)},
    }
    if existing:
        file_id = existing[0]["id"]
        drive.files().update(fileId=file_id, body=metadata, media_body=media, fields="id").execute()
    else:
        metadata["parents"] = [state["drive_folder_id"]]
        file_id = drive.files().create(body=metadata, media_body=media, fields="id").execute()["id"]
    return f"https://drive.google.com/file/d/{file_id}/view"


def public_state(state: dict[str, str]) -> dict[str, str]:
    return {
        "spreadsheet_id": state["spreadsheet_id"],
        "spreadsheet_url": f"https://docs.google.com/spreadsheets/d/{state['spreadsheet_id']}/edit",
        "drive_folder_id": state["drive_folder_id"],
        "drive_folder_url": f"https://drive.google.com/drive/folders/{state['drive_folder_id']}",
    }


def command_bootstrap(args) -> None:
    gmail, drive, sheets = services(interactive=True)
    profile = gmail.users().getProfile(userId="me").execute()
    state = ensure_resources(drive, sheets)
    print(json.dumps({"gmail": profile.get("emailAddress"), **public_state(state)}, indent=2))


def command_sync(args) -> None:
    gmail, drive, sheets = services(interactive=not args.non_interactive)
    state = ensure_resources(drive, sheets)
    result = sync_messages(gmail, sheets, state)
    print(json.dumps({**result, **public_state(state)}, indent=2))


def command_work_items(args) -> None:
    _, drive, sheets = services(interactive=not args.non_interactive)
    state = ensure_resources(drive, sheets)
    rows = [row for row in read_rows(sheets, state["spreadsheet_id"]) if row_needs_work(row)]
    for row in rows:
        row.pop("_row_number", None)
    print(json.dumps(rows, indent=2))


def command_start(args) -> None:
    _, drive, sheets = services(interactive=False)
    state = ensure_resources(drive, sheets)
    row = find_row(sheets, state, args.message_id)
    attempts = int(row.get("Attempt Count") or 0) + 1
    update_row(sheets, state, row, **{"Status": "In Progress", "Attempt Count": attempts, "Last Run IST": now_ist(), "Error": ""})
    print(json.dumps({"message_id": args.message_id, "status": "In Progress", "attempt": attempts}))


def command_publish(args) -> None:
    _, drive, sheets = services(interactive=False)
    state = ensure_resources(drive, sheets)
    row = find_row(sheets, state, args.message_id)
    drive_url = upload_artifact(drive, state, row, Path(args.artifact_dir).resolve())
    update_row(
        sheets,
        state,
        row,
        **{
            "Status": "Pending Review",
            "Reviewer Remarks": "",
            "Implementation Notes": args.notes,
            "GitHub URL": args.github_url,
            "Drive URL": drive_url,
            "Last Run IST": now_ist(),
            "Error": "",
        },
    )
    print(json.dumps({"message_id": args.message_id, "status": "Pending Review", "drive_url": drive_url}))


def command_fail(args) -> None:
    _, drive, sheets = services(interactive=False)
    state = ensure_resources(drive, sheets)
    row = find_row(sheets, state, args.message_id)
    update_row(sheets, state, row, **{"Status": "Failed", "Last Run IST": now_ist(), "Error": args.error[:1000]})
    print(json.dumps({"message_id": args.message_id, "status": "Failed"}))


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)
    bootstrap = sub.add_parser("bootstrap", help="Authorize Google and create Drive/Sheet resources")
    bootstrap.set_defaults(func=command_bootstrap)
    sync = sub.add_parser("sync", help="Import Daily UI emails into the review sheet")
    sync.add_argument("--non-interactive", action="store_true")
    sync.set_defaults(func=command_sync)
    work = sub.add_parser("work-items", help="Print actionable review rows as JSON")
    work.add_argument("--non-interactive", action="store_true")
    work.set_defaults(func=command_work_items)
    start = sub.add_parser("start", help="Mark a challenge In Progress")
    start.add_argument("--message-id", required=True)
    start.set_defaults(func=command_start)
    publish = sub.add_parser("publish", help="Upload an artifact and mark Pending Review")
    publish.add_argument("--message-id", required=True)
    publish.add_argument("--artifact-dir", required=True)
    publish.add_argument("--github-url", required=True)
    publish.add_argument("--notes", default="Implemented and verified")
    publish.set_defaults(func=command_publish)
    fail = sub.add_parser("fail", help="Record a failed attempt")
    fail.add_argument("--message-id", required=True)
    fail.add_argument("--error", required=True)
    fail.set_defaults(func=command_fail)
    return p


def main() -> int:
    args = parser().parse_args()
    try:
        args.func(args)
        return 0
    except Exception as exc:
        print(json.dumps({"error": f"{type(exc).__name__}: {exc}"}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
