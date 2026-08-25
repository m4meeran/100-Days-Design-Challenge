# Day 001 - Clash-Inspired Clan Signup

- **Prompt:** `Prompt: Sign Up - Create a sign up page, modal, form, or app screen related to signing up for something.`
- **Reviewer Remark:** `That something should be Clash of Clan Game Sign up`
- **Implementation focus:** Reworked the signup flow into a Clash of Clans-themed guild registration experience using only custom CSS imagery and no official assets.
- **Design decisions:**
  - Replaced the generic form with a two-panel game-clan onboarding layout.
  - Added clan tag auto-formatting and a live badge preview for immediate feedback.
  - Added stronger inline validation for commander name, tag, email, password, and terms agreement.
  - Kept all visuals custom (no protected or copied assets), with keyboard-focus styles and ARIA-live status updates.
- **Verification:**
  - Verified form behavior via browser validation and custom submit handling paths.
  - Confirmed layout remains usable at desktop and mobile breakpoints (`max-width: 900px`, `max-width: 520px`).
  - Ran project tests: `.venv/bin/python -m pytest`.
