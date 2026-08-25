import base64

from daily_ui_automation import extract_day, extract_message_body, extract_prompt, row_needs_work, sanitize_name


def test_extract_day_from_subject():
    assert extract_day("Daily UI #001 | Sign Up") == 1
    assert extract_day("DailyUI Challenge 42") == 42


def test_extract_day_returns_none_without_number():
    assert extract_day("Welcome to Daily UI") is None


def test_plain_text_body_decoding():
    encoded = base64.urlsafe_b64encode(b"Design a sign-up page").decode().rstrip("=")
    payload = {"mimeType": "text/plain", "body": {"data": encoded}}
    assert extract_message_body(payload) == "Design a sign-up page"


def test_row_needs_work_rules():
    assert row_needs_work({"Status": "New", "Reviewer Remarks": ""})
    assert row_needs_work({"Status": "Changes Requested", "Reviewer Remarks": "Improve contrast"})
    assert row_needs_work({"Status": "Pending Review", "Reviewer Remarks": "Improve contrast"})
    assert not row_needs_work({"Status": "Pending Review", "Reviewer Remarks": ""})
    assert not row_needs_work({"Status": "Approved", "Reviewer Remarks": ""})


def test_sanitize_name():
    assert sanitize_name("Day 01: Sign Up / Login") == "Day-01-Sign-Up-Login"


def test_extract_prompt_from_daily_ui_newsletter():
    body = "[#001]\n\n*Prompt: Sign Up*\n\nCreate a sign up page.\n\nShare your design on Twitter\n\nFooter"
    title, prompt = extract_prompt(body)
    assert title == "Sign Up"
    assert prompt == "Prompt: Sign Up\n\nCreate a sign up page."
