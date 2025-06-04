import csv
from datetime import datetime

CSV_FILE = 'finance.csv'

def init_csv():
    try:
        with open(CSV_FILE, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Type', 'Amount', 'Note'])
    except FileExistsError:
        pass  # File already exists

def add_entry():
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    category = input("Enter category (e.g., Food, Rent, Salary): ")
    trans_type = input("Enter type (Income/Expense): ").capitalize()
    amount = float(input("Enter amount: "))
    note = input("Optional note: ")

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, trans_type, amount, note])
    print("Entry added successfully!")

def view_summary():
    income = 0.0
    expense = 0.0

    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Type'] == 'Income':
                    income += float(row['Amount'])
                elif row['Type'] == 'Expense':
                    expense += float(row['Amount'])

        print(f"\nSummary:")
        print(f"Total Income : ${income:.2f}")
        print(f"Total Expense: ${expense:.2f}")
        print(f"Balance      : ${income - expense:.2f}\n")
    except FileNotFoundError:
        print("No data found. Start by adding entries.")

def menu():
    init_csv()
    while True:
        print("Personal Finance Tracker")
        print("1. Add Entry")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_entry()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    menu()
