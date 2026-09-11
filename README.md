# Personal Finance Tracker

A simple command-line Personal Finance Tracker built with Python.

This project helps users manage their personal income, expenses, and budgets. Financial records are stored in text files so the data remains available after closing the program.

## Features

* Add income records
* Add expense records
* View all income and expense records
* Calculate total income
* Calculate total expenses
* Calculate current balance
* Generate monthly expense reports
* Set budgets for expense categories
* Compare actual expenses with budgets
* Show whether a category is over budget
* Save data to text files
* Load existing data when the program starts
* Create backups of financial data
* Validate user input
* Handle invalid numeric values and missing files

## Income Sources

The available income sources are:

* Salary
* Freelance
* Gift
* Investment
* Other

## Expense Categories

The available expense categories are:

* Food
* Transport
* Shopping
* Rent
* Bills
* Entertainment
* Other

## Project Structure

```text
PersonalFinanceTracker/
│
├── final-project.py
├── income.txt
├── expenses.txt
├── budget.txt
├── backup/
│   ├── income.txt
│   ├── expenses.txt
│   └── budget.txt
│
├── .gitignore
└── README.md
```

### File Description

* `final-project.py` - Main Python program
* `income.txt` - Stores income records
* `expenses.txt` - Stores expense records
* `budget.txt` - Stores category budgets
* `backup/` - Stores backup copies of financial data
* `.gitignore` - Specifies files that should not be tracked by Git
* `README.md` - Project documentation

## How to Run

Make sure Python is installed on your computer.

Clone the repository and run:

```bash
python final-project.py
```

The program will display a menu:

```text
1. Add Income
2. Add Expense
3. View Records
4. Financial Summary
5. Monthly Expense Report
6. Set Budget
7. Budget Report
8. Backup Data
9. Exit
```

Choose an option by entering its number.

## Example

A user can add an income:

```text
Amount: 2500
Source: Salary
Date: 2026-09-10
```

And expenses:

```text
Amount: 500
Category: Food
Date: 2026-09-10

Amount: 300
Category: Transport
Date: 2026-09-11
```

The program can then calculate:

```text
Total Income: 2500
Total Expenses: 800
Balance: 1700
```

## Technologies

* Python
* Text file storage
* Git
* GitHub

## Python Concepts Used

This project uses beginner-level Python concepts, including:

* Variables and data types
* Lists
* Dictionaries
* `if / elif / else`
* `for` loops
* `while` loops
* Functions
* File handling
* `try / except`
* String methods
* Input validation

## Data Storage

The application uses text files to store data:

* `income.txt` stores income records
* `expenses.txt` stores expense records
* `budget.txt` stores budget information

The program loads existing data when it starts and saves new records automatically.

## Backup

The application includes a backup feature that copies the financial data files into the `backup` folder.

This helps prevent data loss and provides a simple way to keep a copy of the stored records.

## Future Improvements

Possible future improvements include:

* Using CSV or JSON for data storage
* Adding stronger date validation
* Adding expense search and filtering
* Adding charts and data visualization
* Adding a graphical user interface
* Adding more detailed financial reports

## Author

Fatemeh Rajabpour
