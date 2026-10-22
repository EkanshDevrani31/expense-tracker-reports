# Expense Tracker with Reports

A command-line expense tracker in **Python** with a **MySQL** database. Expenses are logged by date and
category, inputs are checked before saving, and SQL queries produce monthly and category totals that can be
exported to CSV.

## Features
- Add expenses with date, category, amount and an optional note
- Input checks before saving: valid date (no future dates), positive amount with up to 2 decimals, category from a fixed list
- Monthly totals and category totals (all time, or for a single month) using `GROUP BY` and `SUM`
- Export all expenses, monthly totals or category totals to a CSV file in `reports/`
- Delete an expense by ID

## Tech Stack
Python, MySQL, `mysql-connector-python`, `csv` module

## Project Structure
```
expense-tracker-reports/
├── main.py          # menu and user input
├── expenses.py      # all SQL queries
├── validators.py    # input checks
├── reports.py       # CSV export
├── db.py            # MySQL connection helpers
├── schema.sql       # expenses table
├── sample_data.sql  # optional demo rows
├── requirements.txt
└── .env.example
```

## Setup (VS Code)
1. Install Python 3.10+ and MySQL, then open this folder in VS Code.
2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS / Linux
   ```
3. `pip install -r requirements.txt`
4. Create the table: run `schema.sql` in MySQL Workbench (or `mysql -u root -p < schema.sql`).
   Optionally run `sample_data.sql` to load demo data.
5. Copy `.env.example` to `.env` and enter your MySQL password.
6. Run the app: `python main.py`

## Example Report Query
```sql
SELECT category, SUM(amount)
FROM expenses
GROUP BY category
ORDER BY SUM(amount) DESC;
```
