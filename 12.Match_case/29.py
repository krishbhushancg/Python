print('''1 → Search Book
2 → Issue Book
3 → Return Book
4 → View Issued Books
5 → Exit''')

type=int(input("enter menu option: "))


match type:
    case 1:
        print("Search Book")
    case 2:
        print("Issue Book")
    case 3:
        print("Return Book")
    case 4:
        print("View Issued Books")
    case 5:
        print("Exit")
    case _:
        print("Invalid")