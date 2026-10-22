"""All SQL for the expense tracker lives here."""
from db import execute, fetch_all


def add_expense(expense_date, category, amount, note):
    new_id, _ = execute(
        "INSERT INTO expenses (expense_date, category, amount, note) VALUES (%s, %s, %s, %s)",
        (expense_date, category, amount, note),
    )
    return new_id


def list_expenses():
    return fetch_all(
        "SELECT id, expense_date, category, amount, note FROM expenses ORDER BY expense_date DESC, id DESC"
    )


def delete_expense(expense_id):
    _, deleted = execute("DELETE FROM expenses WHERE id = %s", (expense_id,))
    return deleted


def monthly_totals():
    """Total spent in each month. Returns rows of (YYYY-MM, total)."""
    rows = fetch_all(
        """
        SELECT YEAR(expense_date), MONTH(expense_date), SUM(amount)
        FROM expenses
        GROUP BY YEAR(expense_date), MONTH(expense_date)
        ORDER BY YEAR(expense_date), MONTH(expense_date)
        """
    )
    return [(f"{year}-{month:02d}", total) for year, month, total in rows]


def category_totals(year=None, month=None):
    """Total spent per category, for all time or for one month."""
    if year is None:
        return fetch_all(
            "SELECT category, SUM(amount) FROM expenses GROUP BY category ORDER BY SUM(amount) DESC"
        )
    return fetch_all(
        """
        SELECT category, SUM(amount)
        FROM expenses
        WHERE YEAR(expense_date) = %s AND MONTH(expense_date) = %s
        GROUP BY category
        ORDER BY SUM(amount) DESC
        """,
        (year, month),
    )
