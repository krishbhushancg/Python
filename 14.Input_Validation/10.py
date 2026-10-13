pin=2468
n=int(input("enter number: "))

for i in range(3):
    n=int(input("enter number: "))
    if n==pin:
        print("successful")
else:
    print("access is denied")