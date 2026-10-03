print("1 → Electronics  2 → Clothing")

category=int(input("enter category: "))
match category:
    case 1:
        print("1 → Mobile  2 → Laptop  3 → Headphones")
        product=int(input("enter product number: "))

        match product:
            case 1:
                print("Mobile Selected")
            case 2:
                print("Laptop Selected")
            case 3:
                print("Headphones Selected")
            case _:
                print("Invalid")
            
    case 2:
            print("1 → Shirt  2 → Jeans  3 → Shoes")
            product=int(input("enter product number: "))
    
            match product:
                case 1:
                    print("Shirt Selected")
                case 2:
                    print("Jeans Selected")
                case 3:
                    print("Shoes Selected")
                case _:
                    print("Invalid")

    case _:
        print("Invalid")