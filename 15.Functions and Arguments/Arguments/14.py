def calculate_total(price,quantity):
    total=price*quantity
    return(f"total: ₹{total}")


n=int(input("enter price: "))
m=int(input("enter quantity: "))

print(calculate_total(n,m))
