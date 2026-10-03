
print('''sunny
rainy
cloudy
snowy''')

weather=input("enter weather number: ").lower().strip()

match weather:
    case "sunny":
        print("Wear sunglasses")
    case "rainy":
        print("Carry an umbrella")
    case "cloudy":
        print("Weather may change")
    case "snowy":
       print("Wear warm clothes")
    case _:
        print("unknown weather")

