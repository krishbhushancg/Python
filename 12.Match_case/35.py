print('''1 → Starters
2 → Main Course
3 → Desserts
4 → Drinks''')

category=int(input("enter category: "))
match category:
    case 1:
        print('''1 → Soup
2 → Spring Roll
3 → Garlic Bread''')
        action=int(input("enter food name: "))

        match action:
            case 1:
                print("Soup Selected")
            case 2:
                print("Spring Roll Selected")
            case 3:
                print("Garlic Bread Selected")
            case _:
                print("Invalid")
            
    case 2:
            print('''1 → Pizza
2 → Pasta
3 → Biryani''')
            action=int(input("enter food: "))
    
            match action:
                case 1:
                    print("Pizza Selected")
                case 2:
                    print("Pasta Selected")
                case 3:
                    print("Biryani Selected")
                case _:
                    print("Invalid")

    case 3:
                print('''1 → Ice Cream
2 → Cake
3 → Gulab Jamun''')
                action=int(input("enter food: "))
        
                match action:
                    case 1:
                        print("Ice Cream Selected")
                    case 2:
                        print("Cake Selected")
                    case 3:
                        print("Gulab Jamun Selected")
                    case _:
                        print("Invalid")

    case 4:
                print('''1 → Coffee
2 → Tea
3 → Juice''')
                action=int(input("enter food: "))
        
                match action:
                    case 1:
                        print("Coffee Selected")
                    case 2:
                        print("Tea Selected")
                    case 3:
                        print("Juice Selected")
                    case _:
                        print("Invalid")
    case _:
        print("Invalid")