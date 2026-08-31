# Day 016 - Popup Overlay

- **Prompt:** `Prompt: Pop-up Overlay\n\nIs it for a newsletter sign-up form ? Is it an ad overlay? A gated subscription page such as for premium news or member-only access?`
- **Design decisions:**
  - Chose a **premium newsletter/gated-membership** overlay as the concrete interpretation of the prompt, presenting a realistic signup interruption on top of article content.
  - Implemented a modal-style popup with backdrop and accessible `role="dialog"`, `aria-modal`, labelled title/description, and clear close affordances.
  - Added fully accessible interactions: open/close controls, Escape-to-close, backdrop click close, and robust focus trap while open with return focus to the trigger button after close.
  - Added realistic form behavior with required name/email/consent validation and visible status messaging for error and success states.
  - Designed a polished responsive card with mobile breakpoints, contrast-checked palette, rounded surfaces, and touch-friendly controls.
  - Added timed reopen behavior to mirror realistic recurring campaigns while allowing manual reopening via `Open membership overlay`.
- **Verification:**
  - Manually verified that the overlay opens on load after delay and via `Open membership overlay`.
  - Verified Escape and backdrop close pathways close the overlay and return focus.
  - Verified form validation covers missing name, invalid email format, and unchecked consent.
  - Verified successful submit replaces actions and shows confirmation message.
  - Ran project validations: `.venv/bin/python -m pytest` and `.venv/bin/python -m py_compile daily_ui_automation.py`.
