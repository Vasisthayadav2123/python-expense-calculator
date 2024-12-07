def main():
    print(f"🎯running expense tracker")
    
    get_user_expense()

    save_expense_to_file()

    summarize_expense()

    
# taking input from the user
def get_user_expense():
    print(f"🎯getting user expense")

#saving the expenses to a file
def save_expense_to_file():
    print(f"🎯saving expense to file")

#summarising the expenses 
def summarize_expense():
    print(f"🎯summarising the expenses")


if __name__ == "__main__": 
    main()
