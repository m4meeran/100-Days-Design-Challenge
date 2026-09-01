# Day 018 - Analytics Chart

- **Prompt:**
  `Prompt: Analytics Chart\n\nIs it to be used for web or app usage, e-commerce or traffic analytics? Is it tracking sports or stock market performance?`

- **Design decisions:**
  - Chose a practical **unified analytics dashboard** that can represent web, app usage, and e-commerce traffic while staying close to common product analytics needs.
  - Implemented a single-page, responsive layout with semantic structure (`header`, `main`, `section`, `fieldset`, `legend`) and clear focus styles for keyboard users.
  - Added segmented controls for channel (`Web`, `App`, `Store`) and period (`7 days`, `30 days`, `90 days`) with real data updates to all charts and metrics.
  - Included an interactive trend chart (SVG path + points) and a source mix chart (animated bars), updated with JavaScript for each control change.
  - Added accessible state announcements through `aria-pressed`, explicit legends, and an always-visible status sentence describing current scope.
  - Kept the artifact standalone: pure HTML/CSS/JS with no external libraries or network calls.

- **Verification:**
  - Confirmed controls update cards and charts together for each channel/time-range combination.
  - Confirmed keyboard operability for tabbed channel controls (left/right arrow moves between channel buttons).
  - Checked visual behavior in desktop and narrow viewport assumptions via responsive breakpoints in CSS (`max-width: 860px`, `max-width: 640px`).
  - Ran project checks: `.venv/bin/python -m pytest` and `.venv/bin/python -m py_compile daily_ui_automation.py`.
  - Ran JavaScript syntax check: `node --check challenges/day-018-analytics-chart/script.js`.
