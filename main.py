"""Expense Tracker with Reports (Python + MySQL)."""
import mysql.connector

import expenses
import reports
import validators

MENU = """
===== Expense Tracker =====
 1. Add expense
 2. View all expenses
 3. Delete expense
 4. Monthly totals
 5. Category totals
 6. Export report to CSV
 0. Exit
"""


def ask(prompt, parser):
    """Keep asking until the parser accepts the input."""
    while True:
        try:
            return parser(input(prompt))
        except ValueError as err:
            print(f"  {err}")


def print_table(headers, rows):
    if not rows:
        print("  (no records)")
        return
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell if cell is not None else "")))
    line = " | ".join(h.ljust(widths[i]) for i, h in enumerate(headers))
    print(line)
    print("-" * len(line))
    for row in rows:
        print(" | ".join(str(c if c is not None else "").ljust(widths[i]) for i, c in enumerate(row)))


def add_expense():
    expense_date = ask("Date (YYYY-MM-DD, Enter for today): ", validators.parse_date)
    for number, name in enumerate(validators.CATEGORIES, start=1):
        print(f"  {number}. {name}")
    category = ask("Category (number or name): ", validators.parse_category)
    amount = ask("Amount: ", validators.parse_amount)
    note = ask("Note (optional): ", validators.parse_note)
    new_id = expenses.add_expense(expense_date, category, amount, note)
    print(f"  Expense saved with ID {new_id}.")


def view_expenses():
    print_table(["ID", "Date", "Category", "Amount", "Note"], expenses.list_expenses())


def parse_id(text):
    if not text.strip().isdigit():
        raise ValueError("Enter a valid ID.")
    return int(text)


def delete_expense():
    expense_id = ask("Expense ID to delete: ", parse_id)
    if expenses.delete_expense(expense_id):
        print("  Expense deleted.")
    else:
        print("  Expense not found.")


def show_monthly_totals():
    print_table(["Month", "Total"], expenses.monthly_totals())


def show_category_totals():
    raw = input("Month (YYYY-MM) or press Enter for all time: ").strip()
    if raw:
        try:
            year, month = validators.parse_month(raw)
        except ValueError as err:
            print(f"  {err}")
            return
        rows = expenses.category_totals(year, month)
    else:
        rows = expenses.category_totals()
    print_table(["Category", "Total"], rows)


def export_report():
    print("  1. All expenses\n  2. Monthly totals\n  3. Category totals (all time)")
    choice = input("Which report? ").strip()
    if choice == "1":
        path = reports.write_csv("all_expenses", ["ID", "Date", "Category", "Amount", "Note"], expenses.list_expenses())
    elif choice == "2":
        path = reports.write_csv("monthly_totals", ["Month", "Total"], expenses.monthly_totals())
    elif choice == "3":
        path = reports.write_csv("category_totals", ["Category", "Total"], expenses.category_totals())
    else:
        print("  Invalid choice.")
        return
    print(f"  Report saved to {path}")


ACTIONS = {
    "1": add_expense, "2": view_expenses, "3": delete_expense,
    "4": show_monthly_totals, "5": show_category_totals, "6": export_report,
}


def main():
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        action = ACTIONS.get(choice)
        if not action:
            print("  Invalid option, try again.")
            continue
        try:
            action()
        except mysql.connector.Error as err:
            print(f"  Database error: {err}")


if __name__ == "__main__":
    main()
