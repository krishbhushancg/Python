n=int(input("enter age: "))

while n<0 or n>120:
    print("Invalid Age !! Try Again!")
    n=int(input("enter age: "))

print(f"age: {n}")