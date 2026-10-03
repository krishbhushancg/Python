print("1 → Kilometers to Meters\n" \
"2 → Meters to Kilometers\n" \
"3 → Kilograms to Grams\n" \
"4 → Grams to Kilograms")


conversion=int(input("enter choice: "))
value=int(input("enter value: "))

match conversion:
    case 1:
        result=value*1000
        print(f"result: {result} m")
    case 2:
        result=value/1000
        print(f"result: {result} km")
    case 3:
        result=value*1000
        print(f"result: {result} gm")
    case 4:
        result=value/1000 
        print(f"result: {result} kg")
    case _:
        print("Invalid")