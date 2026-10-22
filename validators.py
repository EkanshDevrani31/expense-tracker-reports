"""Input checks run before anything is saved. Each function raises ValueError with a clear message."""
from datetime import date, datetime
from decimal import Decimal, InvalidOperation

CATEGORIES = ["Food", "Travel", "Rent", "Shopping", "Bills", "Health", "Other"]
MAX_AMOUNT = Decimal("10000000")


def parse_date(text):
    """Accepts YYYY-MM-DD. Empty input means today. Future dates are rejected."""
    text = text.strip()
    if not text:
        return date.today()
    try:
        value = datetime.strptime(text, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format, for example 2026-10-18.")
    if value > date.today():
        raise ValueError("Date cannot be in the future.")
    return value


def parse_amount(text):
    """Positive number with at most 2 decimal places."""
    try:
        value = Decimal(text.strip())
    except InvalidOperation:
        raise ValueError("Amount must be a number, for example 250 or 99.50.")
    if not value.is_finite():
        raise ValueError("Amount must be a number, for example 250 or 99.50.")
    if value <= 0:
        raise ValueError("Amount must be greater than zero.")
    if value > MAX_AMOUNT:
        raise ValueError("Amount is too large.")
    if value != value.quantize(Decimal("0.01")):
        raise ValueError("Amount can have at most 2 decimal places.")
    return value


def parse_category(text):
    """Accepts the category number from the list or its name."""
    text = text.strip()
    if text.isdigit():
        index = int(text) - 1
        if 0 <= index < len(CATEGORIES):
            return CATEGORIES[index]
    for name in CATEGORIES:
        if name.lower() == text.lower():
            return name
    raise ValueError("Choose a category number or name from the list.")


def parse_month(text):
    """Accepts YYYY-MM and returns (year, month)."""
    try:
        parsed = datetime.strptime(text.strip(), "%Y-%m")
    except ValueError:
        raise ValueError("Month must be in YYYY-MM format, for example 2026-10.")
    return parsed.year, parsed.month


def parse_note(text):
    text = text.strip()
    if len(text) > 200:
        raise ValueError("Note must be 200 characters or fewer.")
    return text
