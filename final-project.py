import os
import shutil


#Income sources
sources = [
    "Salary",
    "Prifit",
    "Other"
]


#Expense categories
categories = [
    "Food",
    "Shopping",
    "Rent",
    "Bills",
    "Entertainment",
    "Other"
]


# Store all records
incomes = []
expenses = []
budgets = {}

# Get valid date

def get_date():

    while True:

        date = input("Please enter the date (YYYY-MM-DD): ").strip()

        if len(date) == 10 and date[4] == "-" and date[7] == "-":

            return date

        else:

            print("Invalid date format. Please use YYYY-MM-DD.")


# Load incomes

def load_incomes():

    try:

        with open("income.txt", "r") as file:

            for line in file:

                line = line.strip()

                if line == "":
                    continue

                parts = line.split(",")

                income_record = {
                    "amount": float(parts[0]),
                    "source": parts[1],
                    "date": parts[2]
                }

                incomes.append(income_record)

    except FileNotFoundError:

        print("No previous income records found.")


# Load expenses

def load_expenses():

    try:

        with open("expenses.txt", "r") as file:

            for line in file:

                line = line.strip()

                if line == "":
                    continue

                parts = line.split(",")

                expense_record = {
                    "amount": float(parts[0]),
                    "category": parts[1],
                    "date": parts[2]
                }

                expenses.append(expense_record)

    except FileNotFoundError:

        print("No previous expense records found.")


# Load budgets

def load_budgets():

    try:

        with open("budget.txt", "r") as file:

            for line in file:

                line = line.strip()

                if line == "":
                    continue

                parts = line.split(",")

                category = parts[0]
                budget = float(parts[1])

                budgets[category] = budget

    except FileNotFoundError:

        print("No previous budget records found.")


# Add income

def add_income():

    print()
    print("========== Add Income ==========")


    # Get income amount
    while True:

        try:

            income = float(input("Please enter your income: "))

            if income > 0:
                break

            else:
                print("Income must be greater than 0.")

        except ValueError:

            print("Please enter a valid number.")


    # Get income source
    source = input("Please enter the income source: ").strip()

    while source not in sources:

        print("Invalid source.")
        print("Available sources:", sources)

        source = input("Please enter the income source: ").strip()


    # Get date
    date = get_date()


    # Create income record
    income_record = {
        "amount": income,
        "source": source,
        "date": date
    }


    # Add record to the list
    incomes.append(income_record)


    # Save income to file
    with open("income.txt", "a") as file:

        line = (
            str(income_record["amount"]) + "," +
            income_record["source"] + "," +
            income_record["date"] + "\n"
        )

        file.write(line)


    print()
    print("Income added and saved successfully!")


# Add expense

def add_expense():

    print()
    print("========== Add Expense ==========")


    # Get expense amount
    while True:

        try:

            expense = float(input("Please enter your expense: "))

            if expense > 0:
                break

            else:
                print("Expense must be greater than 0.")

        except ValueError:

            print("Please enter a valid number.")


    # Get expense category
    category = input(
        "Please enter the expense category: "
    ).strip()

    while category not in categories:

        print("Invalid category.")
        print("Available categories:", categories)

        category = input(
            "Please enter the expense category: "
        ).strip()


    # Get date
    date = get_date()


    # Create expense record
    expense_record = {
        "amount": expense,
        "category": category,
        "date": date
    }


    # Add record to the list
    expenses.append(expense_record)


    # Save expense to file
    with open("expenses.txt", "a") as file:

        line = (
            str(expense_record["amount"]) + "," +
            expense_record["category"] + "," +
            expense_record["date"] + "\n"
        )

        file.write(line)


    print()
    print("Expense added and saved successfully!")


# View records

def view_records():

    print()
    print("========== Income Records ==========")


    if len(incomes) == 0:

        print("No income records found.")

    else:

        for income in incomes:

            print(
                "Amount:", income["amount"],
                "| Source:", income["source"],
                "| Date:", income["date"]
            )


    print()
    print("========== Expense Records ==========")


    if len(expenses) == 0:

        print("No expense records found.")

    else:

        for expense in expenses:

            print(
                "Amount:", expense["amount"],
                "| Category:", expense["category"],
                "| Date:", expense["date"]
            )


# Financial summary

def show_summary():

    total_income = 0
    total_expenses = 0


    # Calculate total income
    for income in incomes:

        total_income = total_income + income["amount"]


    # Calculate total expenses
    for expense in expenses:

        total_expenses = total_expenses + expense["amount"]


    # Calculate balance
    balance = total_income - total_expenses


    print()
    print("========== Financial Summary ==========")

    print("Total Income:", total_income)
    print("Total Expenses:", total_expenses)
    print("Balance:", balance)


# Monthly expense report

def monthly_report():

    month = input(
        "Please enter the month (YYYY-MM): "
    ).strip()


    total = 0


    print()
    print("========== Monthly Expense Report ==========")


    for expense in expenses:

        if expense["date"].startswith(month):

            print(
                "Amount:", expense["amount"],
                "| Category:", expense["category"],
                "| Date:", expense["date"]
            )

            total = total + expense["amount"]


    print()
    print("Total expenses for", month, ":", total)


# Set budget

def set_budget():

    print()
    print("========== Set Budget ==========")


    # Get expense category
    category = input(
        "Please enter the expense category: "
    ).strip()


    while category not in categories:

        print("Invalid category.")
        print("Available categories:", categories)

        category = input(
            "Please enter the expense category: "
        ).strip()


    # Get budget amount
    while True:

        try:

            budget = float(
                input("Please enter your budget: ")
            )

            if budget > 0:
                break

            else:
                print("Budget must be greater than 0.")

        except ValueError:

            print("Please enter a valid number.")


    # Save budget in dictionary
    budgets[category] = budget


    # Save all budgets to file
    with open("budget.txt", "w") as file:

        for category in budgets:

            line = (
                category + "," +
                str(budgets[category]) + "\n"
            )

            file.write(line)


    print()
    print("Budget set successfully!")


# Budget report

def check_budget():

    print()
    print("========== Budget Report ==========")


    if len(budgets) == 0:

        print("No budgets found.")

        return


    for category in budgets:

        budget = budgets[category]

        total_expense = 0


        # Calculate actual expense
        for expense in expenses:

            if expense["category"] == category:

                total_expense = (
                    total_expense +
                    expense["amount"]
                )


        # Calculate remaining budget
        remaining = budget - total_expense


        print()
        print("Category:", category)
        print("Budget:", budget)
        print("Actual Expense:", total_expense)
        print("Remaining:", remaining)


        if total_expense > budget:

            print("Status: Over Budget")

        else:

            print("Status: Within Budget")


# Backup data

def backup_data():

    backup_folder = "backup"


    # Create backup folder if it does not exist
    if not os.path.exists(backup_folder):

        os.makedirs(backup_folder)


    files = [
        "income.txt",
        "expenses.txt",
        "budget.txt"
    ]


    for file in files:

        if os.path.exists(file):

            shutil.copy(file, backup_folder)


    print()
    print("Backup completed successfully!")


# Main menu

def main():

    # Load old records
    load_incomes()
    load_expenses()
    load_budgets()


    while True:

        print()
        print("=================================")
        print("     PERSONAL FINANCE TRACKER")
        print("=================================")

        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Records")
        print("4. Financial Summary")
        print("5. Monthly Expense Report")
        print("6. Set Budget")
        print("7. Budget Report")
        print("8. Backup Data")
        print("9. Exit")


        choice = input(
            "Please choose an option: "
        ).strip()


        if choice == "1":

            add_income()


        elif choice == "2":

            add_expense()


        elif choice == "3":

            view_records()


        elif choice == "4":

            show_summary()


        elif choice == "5":

            monthly_report()


        elif choice == "6":

            set_budget()


        elif choice == "7":

            check_budget()


        elif choice == "8":

            backup_data()


        elif choice == "9":

            print("Goodbye!")

            break


        else:

            print("Invalid choice. Please try again.")


# Start program

main()