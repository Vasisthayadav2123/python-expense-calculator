class Expense:
    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = float(amount)

def main():
    print(f"🎯 running expense tracker")
    expense_file_name = "expense.csv"
    
    expense = get_user_expense()
    save_expense_to_file(expense, expense_file_name)
    
    summarize_expense(expense_file_name)

def get_user_expense():
    print(f"🎯 getting user expense")
    
    expense_name = input(f"Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    print(f"{expense_amount}, {expense_name}")
    
    expense_categories = [
        "🍎 food",
        "💼 work",
        "⛽ fuels",
        "🎈 fun",
        "🪢 misc", 
    ]
    category_len = len(expense_categories)
    print(category_len)
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i+1}. {category_name}")  

        try:
            selected_index = int(input(f"Enter the category [1 - {category_len}] : ")) - 1 
        except Exception:
            print("You entered a string/char instead of a number") 

        if selected_index in range(category_len):
            print(f"You selected: {expense_categories[selected_index]}")
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("You entered an invalid category")

def save_expense_to_file(expense: Expense, expense_file_name):
    print(f"🎯 saving expense to file: {expense} to {expense_file_name}")
    with open(expense_file_name, "a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")

def summarize_expense(expense_file_name):
    print(f"🎯 summarizing the expenses in {expense_file_name}")
    expenses = []
    with open(expense_file_name, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")
            print(expense_name, expense_category, expense_amount)
            line_expense = Expense(
                name=expense_name, category=expense_category, amount=expense_amount
            )
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses By Category 📈:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"💵 Total Spent: ${total_spent:.2f}")

if __name__ == "__main__": 
    main()
