from ex import Expense
import calendar
import datetime
def main():
    print("run ho rha hai")
    expense_file_path = "expense.csv"

    budget = int(input("bhai aapka budget hai: "))
    expense = expense_kitna_hua()
    file_m_save_kro(expense, expense_file_path)
    summarize_expenses(budget, expense_file_path)


def expense_kitna_hua():
    print("kitna kharcha kiya h")
    expense_name = input("kha kharcha kiya bolo: ")
    expense_amount = float(input("kitne paise yaha p udaye h: pi"))
    print(f"expense name is {expense_name}, {expense_amount}")


    expense_cateories = [
        "Transport",
        "Food",
        "Home",
        "Work",
        "Fun",
        "Misc"
    ]

    while True:
        print("kis category m kharcha kr rhe ho batao: ")
        for i, category_name in enumerate(expense_cateories):
            print(f"{i+1}. {category_name}")

        value_range = f"[1-{len(expense_cateories)}]"
        selected_index = int(input(f"bhai category bata do: {value_range} "))-1

        if selected_index in range(len(expense_cateories)):
            selected_category = expense_cateories[selected_index]
            print(selected_category)

            new_expense = Expense(name = expense_name,amount = expense_amount,category = selected_category)

            return new_expense
        
        else:
            print("invalid input")


        break





def file_m_save_kro(expense :Expense,expense_file_path):

    print(f"kharcha file m save krna h : {expense} to {expense_file_path}")
    with open(expense_file_path,"a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expenses(budget, expense_file_path):
    print("kharcha summary")
    expenses = []
    with open(expense_file_path,'r') as f:
        for line in f.readlines():
            expense_name, expense_amount, expense_category =line.strip().split(",")
            print(f"{expense_name} {expense_amount} {expense_category}")
            line_expense = Expense(name = expense_name,amount = float(expense_amount),category = expense_category)
            #print(line_expense)
            expenses.append(line_expense)
    
    amount_by_category = {}
    for expense in expenses:
        key = expense.category

        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    
    # print(amount_by_category)
    print("y aapka catgory wise kharcha hai")
    for key, amount in amount_by_category.items():
        print(key,amount)

    total_spent = sum(amount_by_category.values())
    print(f"y aapka total kharcha hai : {total_spent}")

    remaining_budget = budget - total_spent
    print(f"your remaining budget: {remaining_budget}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]

    remaining_days = (days_in_month) - (now.day)
    print(f"y aapka remaining days hai : {remaining_days}")

    daily_allowance = remaining_budget / remaining_days
    print(red(f"y aapka daily allowance hai : {daily_allowance}"))

def red(text):
    return f"\033[31m{text}\033[0m"

    # for category in set([expense.category for expense in expenses]):
    #     print("total expense for",category)
    #     print(f"{category} : {sum([expense.amount for expense in expenses if expense.category == category])}")

    

if __name__ == "__main__":
    main()