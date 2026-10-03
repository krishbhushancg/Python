print("1 → Vegetarian  2 → Non-Vegetarian")

category=int(input("enter food type: "))
match category:
    case 1:
        print("1 → Paneer  2 → Dal  3 → Veg Biryani")
        product=int(input("enter food: "))

        match product:
            case 1:
                print("Paneer Selected")
            case 2:
                print("Dal Selected")
            case 3:
                print("Veg Biryani Selected")
            case _:
                print("Invalid")
            
    case 2:
            print("1 → Chicken Biryani  2 → Chicken Curry  3 → Fish Fry")
            product=int(input("enter food: "))
    
            match product:
                case 1:
                    print("Chicken Biryani Selected")
                case 2:
                    print("Chicken Curry Selected")
                case 3:
                    print("Fish Fry Selected")
                case _:
                    print("Invalid")

    case _:
        print("Invalid")