# Day 003 - Landing Page

- **Prompt:** `Prompt: Landing Page - What's the main focus? ... consider important landing page elements (Headlines, call-to-action buttons, typography, clarity, etc.)`
- **Design decisions:**
  - Built a campaign-focused landing page with hero, nav, feature cards, and testimonial interaction.
  - Added clear hierarchy with heading, kicker, CTA, and supporting blocks.
  - Implemented accessible show/hide testimonial for secondary content without script-only illusions.
- **Verification:**
  - Confirmed hero and feature cards collapse from desktop three-column to single-column.
  - Tested testimonial toggle and keyboard focus order by manual interaction.
  - Ran `.venv/bin/python -m pytest` and `.venv/bin/python -m py_compile daily_ui_automation.py`.