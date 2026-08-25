# Day 004 - Calculation

- **Prompt:** `Prompt: Calculation - Design a calculation element or interface` (standard/scientific/financial variants accepted)
- **Design decisions:**
  - Built a fully interactive calculator with digit, operator, equals, sign, clear, and backspace actions.
  - Added a small expression history line so users can review the prior computation.
  - Kept control targets large and spaced for touch usability on mobile.
  - Added safe expression evaluation pattern and visible error handling.
- **Verification:**
  - Tested arithmetic and control buttons by manual interaction.
  - Confirmed keypad adapts cleanly on narrow and wide screens.
  - Ran `.venv/bin/python -m pytest` and `.venv/bin/python -m py_compile daily_ui_automation.py`.