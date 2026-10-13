n=int(input("enter product quantity: "))
m=int(input("enter product unit price: "))

while n<0 or m<0:
    n=int(input("enter product quantity: "))
    m=int(input("enter product unit price: "))

print(f"product unit price: {m}")
print(f"product quantity: {n}")
print(f"total cost: {m*n}")