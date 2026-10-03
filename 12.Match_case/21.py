
print("1 → Celsius to Fahrenheit  2 → Fahrenheit to Celsius")
choice=int(input("enter choice: "))
temp=int(input("enter temp: "))

operation=int(input("enter operation number: "))
match choice:
    case 1:
        result=((temp*9)/5)+32
        print(f"temperature: {result} F")
    case 2:
        result=((temp-32)*5)/9
        print(f"temperature: {result} C")
    case _:
        print("Invalid")