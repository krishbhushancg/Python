print('''1 → General Medicine
2 → Cardiology
3 → Orthopedics
4 → Pediatrics
5 → Emergency''')

type=int(input("enter department: "))


match type:
    case 1:
        print("General Medicine Department")
    case 2:
        print("Cardiology Department")
    case 3:
        print("Orthopedics Department")
    case 4:
        print("Pediatrics Department")
    case 5:
        print("Emergency Department")
    case _:
        print("Invalid")