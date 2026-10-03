a=0
b=0
c=0
d=0


for i in range(8):
    name=input(f"enter name of product {i+1}: ")
    quantity=int(input(f"enter quantity of product {i+1}: "))

    if quantity>20:
        print("available")
        a+=1
    elif quantity<=20 and quantity>=6:
        print("low")
        b+=1
    elif quantity<=5 and quantity>=1:
        print("critical")
        c+=1
    elif quantity==0:
        print("out of stock")
        d+=1

print(f"out of stock products: {d}")
print(f"critical products: {c}")
print(f"low products: {b}")
print(f"available products: {a}")

