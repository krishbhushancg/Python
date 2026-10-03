print('''1 → Account Balance
2 → Mini Statement
3 → Fund Transfer
4 → Bill Payment
5 → Customer Support''')

banking=int(input("enter shopping number: "))
match banking:
    case 1:
        print("Opening Electronics")
    case 2:
        print("Opening Clothing")
    case 3:
        print("Opening Books")
    case 4:
        print("Opening Grocery")
    case 5:
        print("Exit")
    case _:
        print("Invalid")
