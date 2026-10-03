print('''1 → Engine
2 → Lights
3 → Music
4 → Navigation''')

category=int(input("enter category: "))
match category:
    case 1:
        print('''1 → Start
2 → Stop''')
        action=int(input("enter action: "))

        match action:
            case 1:
                print("Start selected")
            case 2:
                print("Stop Selected")
            case _:
                print("Invalid")
            
    case 2:
            print('''1 → Headlights
2 → Indicators
3 → Hazard Lights''')
            action=int(input("enter lights name: "))

            match action:
                case 1:
                    print("Headlights Selected")
                case 2:
                    print("Indicators Selected")
                case 3:
                    print("Hazard Lights selected")
                case _:
                    print("Invalid")

    case 3:
                print('''1 → Play
2 → Pause
3 → Next
4 → Previous''')
                action=int(input("enter action: "))
        
                match action:
                    case 1:
                        print("Play selcted: ")
                    case 2:
                        print("Pause selcted")
                    case 3:
                        print("Next selected")
                    case 4:
                        print("Previous selected")
                    case _:
                        print("Invalid")
    case _:
        print("Invalid")