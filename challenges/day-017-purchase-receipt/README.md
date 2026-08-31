# Day 017 - Purchase Receipt

- **Prompt:** `Prompt: Purchase Receipt\n\nWhat was purchased? On what date? How much was the item? And from what source and vendor? Consider other elements such as a customer support info, a tracking number or receipt number, business location/phone number/website, pictures if needed, and any other related elements.`
- **Design decisions:**
  - Implemented a realistic e-commerce purchase receipt page with a clear merchant header and order identifiers.
  - Included all required fields: purchased items, date, total amount, source, vendor/location/website, tracking number, and receipt number.
  - Added explicit support section with phone, email, hours, and vendor details.
  - Added a copyable receipt number interaction and expandable shipping timeline for realistic logistics context.
  - Designed a responsive two-column receipt card layout with mobile stacking, accessible table semantics, high-contrast controls, and semantic landmarks.
  - Kept all interactions keyboard-accessible (`button`, `a`, and status updates are announced with `aria-live`).
- **Verification:**
  - Verified layout renders on a desktop and mobile viewport.
  - Verified shipping timeline toggle updates `aria-expanded` and visibility.
  - Verified receipt number copy control updates status message.
  - Ran project validation commands: `.venv/bin/python -m pytest` and `.venv/bin/python -m py_compile daily_ui_automation.py`.
