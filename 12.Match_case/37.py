print('''1 → Programming
2 → Mathematics
3 → Communication''')

category=int(input("enter category: "))
match category:
    case 1:
        print('''1 → Python
2 → Java
3 → C++''')
        action=int(input("enter program name: "))

        match action:
            case 1:
                print("Python selected")
            case 2:
                print("Java Selected")
            case 3:
                print("C++ selected")
            case _:
                print("Invalid")
            
    case 2:
            print('''1 → Algebra
2 → Calculus
3 → Statistics''')
            action=int(input("enter topic name: "))

            match action:
                case 1:
                    print("Algebra Selected")
                case 2:
                    print("Calculus Selected")
                case 3:
                    print("Statistics selected")
                case _:
                    print("Invalid")

    case 3:
                print('''1 → English
2 → Presentation
3 → Interview Skills''')
                action=int(input("enter topic: "))
        
                match action:
                    case 1:
                        print("English selcted: ")
                    case 2:
                        print("Presentation selcted")
                    case 3:
                        print("Interview Skills selected")
                    case _:
                        print("Invalid")
    case _:
        print("Invalid")