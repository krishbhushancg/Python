print('''1 → Start Game
2 → Load Game
3 → Settings
4 → Exit''')

type=int(input("enter menu option: "))


match type:
    case 1:
        print("Start Game selected")
    case 2:
        print("Load Game selected")
    case 3:
        print("Settings selected")
        print('''1 → Sound
2 → Graphics
3 → Controls''')
        action=int(input("enter action: "))
        match action:
            case 1:
                print("sound settings")
            case 2:
                print("Graphics settings")
            case 3: 
                print("Controls settings")
    case 4:
        print("exiting...")
    case _:
        print("Invalid")