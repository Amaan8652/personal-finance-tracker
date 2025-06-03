
# personal-expense-tracker
This is my first git repository.
A Python command-line application for tracking personal income and expenses with data visualization and monthly reporting features.
#!/usr/bin/env python3
"""
Personal Expense Tracker
A simple CLI application to track daily expenses with categories and analytics.
"""

from expense_tracker import ExpenseTracker
import sys

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses") 
        print("3. View Summary")
        print("4. View by Category")
        print("5. Export to CSV")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            add_expense_menu(tracker)
        elif choice == '2':
            tracker.display_expenses()
        elif choice == '3':
            tracker.display_summary()
        elif choice == '4':
            category = input("Enter category: ").strip()
            tracker.display_by_category(category)
        elif choice == '5':
            filename = input("Enter filename (without .csv): ").strip()
            tracker.export_to_csv(f"{filename}.csv")
        elif choice == '6':
            print("Thanks for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_expense_menu(tracker):
    try:
        amount = float(input("Enter amount: $"))
        category = input("Enter category (food/transport/entertainment/bills/other): ").strip().lower()
        description = input("Enter description:
