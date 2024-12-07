import expense from expense

def main():
    print(f"🎯running expense tracker")
    
    get_user_expense()

    save_expense_to_file()

    summarize_expense()

    
# taking input from the user
def get_user_expense():

    print(f"🎯getting user expense")
    
    expense_name = input(f"enter expense name:" )
    expense_amount = float(input("enter expense amount: "))
    print(f"{expense_amount},{expense_name}")
    
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

        print("select a category: ")

        for i, category_name in enumerate(expense_categories):
            print(f"    {i+1}. {category_name}")  


        try:    

            selected_category = int(input(f"enter the category [1 - {category_len}] : ")) - 1 
        except Exception:

            print("you entered an string/char instead of number") 


        if selected_category in range (category_len):

            print(f" you selected: {expense_categories[selected_category]}")


            break
        else:
            print("you entered and invalid catgory")

#saving the expenses to a file
def save_expense_to_file():
    print(f"🎯saving expense to file")

#summarising the expenses 
def summarize_expense():
    print(f"🎯summarising the expenses")


if __name__ == "__main__": 
    main()
