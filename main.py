
import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


# Create CSV file if it does not exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Amount", "Category", "Date"])


def add_expense():
    print("\n--- Add New Expense ---")

    title = input("Enter expense title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    try:
        amount = float(input("Enter expense amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    
    category = input("Enter category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    date = input("Enter date (DD-MM-YYYY): ").strip()

    try:
        datetime.strptime(date, "%d-%m-%Y")
    except ValueError:
        print("Invalid date! Please enter a valid date in DD-MM-YYYY format.")
        return


    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([title, amount, category, date])

    print("Expense added and saved successfully!")


def view_expenses():
    print("\n--- All Expenses ---")

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        expenses = list(reader)

    if not expenses:
        print("No expenses recorded yet.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['Title']} | "
            f"Rs. {expense['Amount']} | "
            f"{expense['Category']} | {expense['Date']}"
        )
        
def search_by_category():
    category = input("Enter category to search: ").strip()

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        found = False

        print("\n--- Search Results ---")

        for expense in reader:
            if expense["Category"].lower() == category.lower():
                print(
                    f"Title: {expense['Title']} | "
                    f"Amount: Rs. {expense['Amount']} | "
                    f"Category: {expense['Category']} | "
                    f"Date: {expense['Date']}"
                )
                found = True

        if not found:
            print("No expenses found in this category.")



def calculate_total():
    total = 0

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            total += float(expense["Amount"])

    print("\n===== EXPENSE SUMMARY =====")
    print("Total Expenses: Rs.", round(total, 2))


def monthly_summary():
    month = input("Enter month (MM-YYYY): ").strip()
    total = 0
    found = False

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            date = expense["Date"]

            if len(date) == 10 and date[3:10] == month:
                total += float(expense["Amount"])
                found = True

    print("\n===== MONTHLY SUMMARY =====")

    if found:
        print(f"Total expenses for {month}: Rs. {round(total, 2)}")
    else:
        print("No expenses found for this month.")

        
def delete_expense():
    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        expenses = list(reader)

    if not expenses:
        print("No expenses available to delete.")
        return

    print("\n--- Delete Expense ---")

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['Title']} | "
            f"Rs. {expense['Amount']} | "
            f"{expense['Category']} | {expense['Date']}"
        )

    try:
        choice = int(input("Enter expense number to delete: "))

        if choice < 1 or choice > len(expenses):
            print("Invalid expense number.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    deleted = expenses.pop(choice - 1)

    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["Title", "Amount", "Category", "Date"]
        )
        writer.writeheader()
        writer.writerows(expenses)

    print(f"Deleted expense: {deleted['Title']}")


  

def main():
    while True:
        print("\n===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search by Category")
        print("4. Calculate Total Expenses")
        print("5. Monthly summary")
        print("6. Delete Expense")
        print("7. Exit")
     

        choice = input("Enter your choice: ").strip()

       
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_by_category()
        elif choice == "4":
            calculate_total()
        elif choice == "5":
            monthly_summary()
            
        elif choice == "6":
            delete_expense()
        elif choice == "7":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1 to 7.")

        


if __name__ == "__main__":
    main()
