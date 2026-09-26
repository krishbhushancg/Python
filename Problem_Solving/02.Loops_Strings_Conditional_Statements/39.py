total=0

for i in range(8):
    age=int(input(f"Enter age passenger {i+1}: "))
    distance=int(input(f"Enter distance passenger {i+1}: "))

    fare=10*distance

    if age<5:
        print("free")
    elif age>=5 and age<=12:
        print("50% Discount")
        fare=0.5*fare
        print(f"fare: ₹{fare}")
        total+=fare
    elif age>60:
        print(f"30% Discount")
        fare=0.7*fare
        print(f"fare: ₹{fare}")
        total+=fare
    else:
        print("Full Fare")
        fare=fare
        print(f"fare: ₹{fare}")
        total+=fare
    print()

print(f"total fare: ₹{total}")
