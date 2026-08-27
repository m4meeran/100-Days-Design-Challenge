# Day 014 - Countdown Timer

- **Prompt:** `Prompt: Countdown Timer\n\nIs it for an app? An interface for an oven or cooking device? A sport related countdown such as on a scoreboard? Or is it a launch countdown for NASA, race cars, or something else?`
- **Design decisions:**
  - Built a focused control-first countdown experience for a reusable event timer, with clear controls for naming an event, setting a target time, and using quick preset durations.
  - Prioritized accessibility by using semantic form markup, labeled controls, a visible focus style, and polite/assertive live regions for status and completion announcements.
  - Added practical timer behavior (start, pause/resume, reset) with safeguards for invalid dates and minimum duration so users always get valid feedback.
  - Implemented a responsive two-panel layout that stacks on small screens and uses accessible contrast, large timing numerals, and a progress indicator for quick at-a-glance state.
  - Added support for both fixed target times and quick presets (5/10/20/30 minutes) to make the component adaptable to cooking, study, launch-style, and productivity use cases from the prompt.
- **Verification:**
  - Verified preset button updates the target datetime and starts a timer that decrements every second.
  - Verified entering a past datetime shows an inline error and does not start the countdown.
  - Verified pause/resume toggles remaining time correctly and reset returns the timer to the initial state.
  - Verified completion triggers `Time's up` messaging and sets status to `Complete`, with assistive announcements in the status region.
  - Ran `.venv/bin/python -m pytest` and `.venv/bin/python -m py_compile daily_ui_automation.py`.