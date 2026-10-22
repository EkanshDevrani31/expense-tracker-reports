-- Optional: load a few rows so the reports have something to show.
USE expense_tracker;

INSERT INTO expenses (expense_date, category, amount, note) VALUES
('2026-08-03', 'Food',     250.00, 'Groceries'),
('2026-08-10', 'Travel',   120.00, 'Bus pass'),
('2026-08-21', 'Bills',    799.00, 'Internet'),
('2026-09-02', 'Food',     310.50, 'Dinner with friends'),
('2026-09-14', 'Shopping', 1499.00, 'Headphones'),
('2026-09-28', 'Travel',   450.00, 'Train ticket'),
('2026-10-05', 'Food',     180.00, 'Lunch'),
('2026-10-12', 'Bills',    799.00, 'Internet');
