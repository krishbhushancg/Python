def bill(item, quantity=1, price=100):
    return(f"bill of {item}:{quantity*price}")


n=(input("enter item name: "))
m=int(input("enter quantity: "))
o=int(input("enter price: "))

print(bill(n,m,o))