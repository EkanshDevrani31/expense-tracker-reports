CREATE DATABASE IF NOT EXISTS expense_tracker;
USE expense_tracker;

CREATE TABLE IF NOT EXISTS expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    expense_date DATE NOT NULL,
    category VARCHAR(30) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0),
    note VARCHAR(200)
);
