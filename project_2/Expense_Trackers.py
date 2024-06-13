def main():
    print("j")

    expense_kitna_hua()
    file_m_save_kro()
    summarize_expenses()






def expense_kitna_hua():
    print("kitna kharcha kiya h")
    expense_name = input("kha kharcha kiya bolo: ")
    expense_amount = float(input("kitne paise yaha p udaye h: pi"))
    print(f"expense name is {expense_name}, {expense_amount}")


    expense_cateories = [

        "Food",
        "Home",
        "Work",
        "Fun",
        "Misc"
    ]

def file_m_save_kro():
    pass

def summarize_expenses():
    pass

if __name__ == "__main__":
    main()