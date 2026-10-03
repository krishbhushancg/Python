print('''red
yellow
green''')
traffic=input("enter signal: ").lower().strip()
match traffic:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid Signal")
