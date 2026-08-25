# Day 002 - Payment Gateway Checkout

- **Prompt:** `Prompt: Credit Card Checkout - Design a credit card checkout form or page. Don't forget the important elements such as the numbers, dates, security numbers, etc.`
- **Reviewer Remark:** `This UI/UX should replicate razorpay gateway`
- **Implementation focus:** Deliver a Razorpay-inspired checkout pattern while explicitly stating it is a demo and not brand-affiliated.
- **Design decisions:**
  - Preserved robust checkout functionality (contact, amount, method selection) and expanded to card/UPI/wallet flows.
  - Added dynamic payment method switching with mode-specific required fields and focused validation rules.
  - Added live convenience fee and total calculation, plus custom visual states for errors/success.
  - Kept the interface keyboard-friendly, semantic, and responsive.
- **Verification:**
  - Manual validation of valid/invalid flows for card/UPI/wallet and form reset behavior.
  - Confirmed responsive behavior at mobile widths via stylesheet breakpoints.
  - Ran project tests: `.venv/bin/python -m pytest`.
