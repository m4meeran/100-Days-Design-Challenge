# Day 013 - Direct Message

- **Prompt:** `Prompt: Direct Message\n\nDesign a Direct Messaging app, profile, or chat box. Consider the parties involved in the messages, images, placement, and context of the messages. Are the messages for social purposes? Customer support?`
- **Design decisions:**
  - Built a split-layout Direct Message interface with a conversation list and contextual message thread to represent both support and team chat scenarios.
  - Added accessible semantic structure with an explicit conversation list, message stream, and composer form labels, plus keyboard support for Enter-to-send and focus-visible outlines.
  - Implemented functional interaction points: switch threads, send messages, quick-reply inserter, message timestamps, and delivery/read status updates in the local thread data model.
- **Verification:**
  - Verified thread switching loads independent message histories and preserves UI state.
  - Verified sending a message appends it to the active thread, clears composer input, and updates the chat stream for immediate feedback.
  - Verified Enter key sends message and shift+enter does not send (typed newline support is not currently requested because input is single-line for this compact UI).
  - Ran `.venv/bin/python -m pytest` and `.venv/bin/python -m py_compile daily_ui_automation.py`.
