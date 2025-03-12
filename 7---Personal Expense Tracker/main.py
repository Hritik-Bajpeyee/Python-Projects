import sqlite3
from datetime import datetime

# Connect to SQLite database
conn = sqlite3.connect('expense_tracker.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,  -- 'income' or 'expense'
    amount REAL NOT NULL,
    description TEXT,
    date TEXT NOT NULL
)
''')

# Function to print colored text
def print_color(text, text_color="reset", bg_color=None, bold=False):
    colors = {
        "reset": "\033[0m",
        "black": "\033[30m", "red": "\033[91m", "green": "\033[92m",
        "yellow": "\033[93m", "blue": "\033[94m", "magenta": "\033[95m",
        "cyan": "\033[96m", "white": "\033[97m",
        "gray": "\033[90m", "light_red": "\033[91m", "light_green": "\033[92m",
        "light_yellow": "\033[93m", "light_blue": "\033[94m", 
        "light_magenta": "\033[95m", "light_cyan": "\033[96m"
    }
    
    bg_colors = {
        "black": "\033[40m", "red": "\033[41m", "green": "\033[42m",
        "yellow": "\033[43m", "blue": "\033[44m", "magenta": "\033[45m",
        "cyan": "\033[46m", "white": "\033[47m",
        "light_gray": "\033[100m", "light_red": "\033[101m",
        "light_green": "\033[102m", "light_yellow": "\033[103m",
        "light_blue": "\033[104m", "light_magenta": "\033[105m",
        "light_cyan": "\033[106m"
    }
    
    text_code = colors.get(text_color, colors["reset"])
    bg_code = bg_colors.get(bg_color, "")
    bold_code = "\033[1m" if bold else ""

    print(f"{bold_code}{bg_code}{text_code}{text}{colors['reset']}")

conn.commit()

# Function to add a transaction
def add_trans(trans_type, amt, descrip):
    date = datetime.now().strftime('%Y-%m-%d')
    cursor.execute("INSERT INTO transactions (type, amount, description, date) VALUES (?, ?, ?, ?)", 
                   (trans_type, amt, descrip, date))
    conn.commit()
    print_color(f"{trans_type.capitalize()} of ₹{amt} added successfully!", "green", None, True)

# Function to show monthly summary
def show_month_summary(month, year):
    cursor.execute("""
        SELECT type, SUM(amount) FROM transactions 
        WHERE strftime('%m', date) = ? AND strftime('%Y', date) = ?
        GROUP BY type
    """, (f"{month:02d}", str(year)))
    
    results = cursor.fetchall()
    total_income, total_expense = 0, 0
    
    for trans_type, total in results:
        if trans_type == 'income':
            total_income = total
        elif trans_type == 'expense':
            total_expense = total
    
    balance = total_income - total_expense
    
    print_color(f"\n--- Monthly Summary for {month:02d}/{year} ---", "yellow", "blue", True)
    print_color(f"Total Income: ₹{total_income}", "green")
    print_color(f"Total Expense: ₹{total_expense}", "red")
    print_color(f"Balance: ₹{balance}", "cyan")

# Function to list all transactions
def list_trans():
    cursor.execute('SELECT * FROM transactions ORDER BY date DESC')
    rows = cursor.fetchall()
    
    print_color("\n--- All Transactions ---", "yellow", "blue", True)
    
    for row in rows:
        trans_type = "Income" if row[1] == "income" else "Expense"
        color = "green" if row[1] == "income" else "red"
        print_color(f"ID: {row[0]} | {trans_type}: ₹{row[2]} | {row[3]} | Date: {row[4]}", color)

# Main Menu
def main():
    print_color("\n--- Personal Expense Tracker ---\n", "yellow", "red", True)
    
    while True:
        print_color("1. Add Income", "white", "green")
        print_color("2. Add Expense", "white", "red")
        print_color("3. Show Monthly Summary", "white", "blue")
        print_color("4. View All Transactions", "white", "magenta")
        print_color("5. Exit", "white", "red")
        
        choice = input("\nEnter Your Choice: ")

        if choice == '1':
            amt = float(input("Enter Income Amount: "))
            descrip = input("Enter Description: ")
            add_trans('income', amt, descrip)
        elif choice == '2':
            amt = float(input("Enter Expense Amount: "))
            descrip = input("Enter Description: ")
            add_trans('expense', amt, descrip)
        elif choice == '3':
            month = int(input("Enter Month (1-12): "))
            year = int(input("Enter Year (e.g., 2025): "))
            show_month_summary(month, year)
        elif choice == '4':
            list_trans()
        elif choice == '5':
            print_color("\nExiting... Thank You! 🎉", "white", "red", True)
            break
        else:
            print_color("Invalid Choice! Try Again.", "red")

if __name__ == '__main__':
    main()
