n=int(input("enter marks: "))

while n<0 or n>100:
    print("invalid try again")
    n=int(input("enter marks: "))

print(f"marks: {n}")