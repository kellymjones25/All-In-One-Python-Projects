def add_expense(expenses):
    """
    Add a new expense to the list.
    Each expense is stored as (category, amount).
    """
    category = input("Enter expense category (e.g., Food, Transport): ")
    amount = float(input("Enter expense amount: $"))
    expenses.append((category, amount))
    print(f"✅ Added: {category} - ${amount:.2f}")


def set_budget():
    """
    Ask user to set a budget.
    """
    budget = float(input("Enter your total budget: $"))
    print(f"✅ Budget set: ${budget:.2f}")
    return budget


def view_summary(expenses, budget):
    """
    Show total spending and remaining budget.
    """
    total_spent = sum(amount for _, amount in expenses)
    print("\n📊 Expense Summary")
    print("-" * 25)
    for category, amount in expenses:
        print(f"{category}: ${amount:.2f}")
    print("-" * 25)
    print(f"Total Spent: ${total_spent:.2f}")
    print(f"Remaining Budget: ${budget - total_spent:.2f}\n")


def run_dashboard():
    """
    Main loop for the finance dashboard.
    """
    expenses = []
    budget = 0.0

    while True:
        print("\n=== Personal Finance Dashboard ===")
        print("1. Set Budget")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            budget = set_budget()
        elif choice == "2":
            add_expense(expenses)
        elif choice == "3":
            if budget == 0:
                print("⚠️ Please set a budget first.")
            else:
                view_summary(expenses, budget)
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    run_dashboard()
