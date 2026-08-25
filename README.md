# 100 Days Design Challenge Automation

This repository turns Daily UI emails into reviewed, versioned design artifacts.

## Workflow

1. Gmail messages matching the configured Daily UI query are imported into a Google Sheet.
2. New challenges, failed attempts, and reviewed rows with remarks become actionable.
3. The weekday Hermes job implements one actionable challenge in `challenges/`.
4. The implementation is tested, committed, and pushed to GitHub.
5. A ZIP is uploaded to Google Drive and the Sheet row moves to `Pending Review`.
6. The reviewer either sets `Approved`, or adds remarks while leaving `Pending Review`/selecting `Changes Requested`; the next run applies those remarks.

A `Pending Review` row without remarks waits safely for review and is not rebuilt repeatedly.

## Review sheet columns

`Day`, `Challenge`, `Prompt`, `Email Date`, `Gmail Message ID`, `Status`, `Reviewer Remarks`, `Implementation Notes`, `GitHub URL`, `Drive URL`, `Last Run IST`, `Attempt Count`, `Error`.

Statuses: `New`, `In Progress`, `Pending Review`, `Changes Requested`, `Approved`, `Failed`.

## Secure setup

The OAuth desktop-client JSON, generated token, and local state are ignored by git. Never commit or share these files.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python daily_ui_automation.py bootstrap
.venv/bin/python daily_ui_automation.py sync
.venv/bin/python daily_ui_automation.py work-items
```

## Worker commands

```sh
# Mark the selected row as being implemented
.venv/bin/python daily_ui_automation.py start --message-id MESSAGE_ID

# After creating and verifying challenges/day-NNN-slug
.venv/bin/python daily_ui_automation.py publish \
  --message-id MESSAGE_ID \
  --artifact-dir challenges/day-NNN-slug \
  --github-url GITHUB_TREE_URL \
  --notes "Implementation and verification summary"

# Record an error so the next weekday run can retry
.venv/bin/python daily_ui_automation.py fail --message-id MESSAGE_ID --error "Failure details"
```

## Schedule

Hermes cron runs at `0 13 * * 1-5` in the host timezone, which is verified as IST on this machine. The job processes at most one challenge each run to keep commits and review rows isolated.

## Tests

```sh
.venv/bin/python -m pytest
.venv/bin/python -m py_compile daily_ui_automation.py
```
