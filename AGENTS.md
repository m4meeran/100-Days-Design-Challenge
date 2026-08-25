# Daily UI Autonomous Worker

This repository is operated by a scheduled Hermes Agent run.

## Required run sequence

1. Run `.venv/bin/python daily_ui_automation.py sync --non-interactive`.
2. Run `.venv/bin/python daily_ui_automation.py work-items --non-interactive` and parse the JSON.
3. If no item is actionable, finish without changing git or Google resources.
4. Select exactly one item: lowest numeric Day first. Read the complete Prompt and Reviewer Remarks.
5. Pull `main` with fast-forward only, then run `start --message-id ...`.
6. Implement a polished, responsive, accessible standalone web design under `challenges/day-NNN-slug/`. Include at least `index.html`, `styles.css` when styles are not inline, and a challenge README recording prompt, design decisions, and verification. Do not use placeholder prose or claim interactions that do not work.
7. If Reviewer Remarks exist, treat every remark as an acceptance criterion and preserve working behavior from the previous version.
8. Preview or validate the artifact. At minimum run HTML/JS checks available locally and inspect key mobile/desktop behavior; use a browser screenshot when browser tools are available.
9. Run project tests and inspect `git diff`. Never stage OAuth files, tokens, state, caches, or unrelated files.
10. Commit with `feat(day-NNN): implement <challenge>` or `fix(day-NNN): apply review feedback`, push `main`, and capture the real commit SHA.
11. Run `publish` using the artifact directory and a GitHub tree URL pinned to that commit. This uploads the ZIP to Drive and changes the Sheet row to `Pending Review`.
12. If implementation fails after `start`, call `fail` with a concise real error so a later weekday run can retry.

## Review semantics

- `New`, `Failed`, and `Changes Requested` are actionable.
- `Pending Review` is actionable only when Reviewer Remarks is non-empty.
- `Pending Review` without remarks waits for the user.
- `Approved` is final and must never be modified.
- Process at most one challenge per cron run.

## Security

Never print, read into chat, commit, or upload `credentials.json`, `client_secret_*.json`, `token.json`, or `state.json`. Do not force-push, reset history, or delete existing challenge work.
