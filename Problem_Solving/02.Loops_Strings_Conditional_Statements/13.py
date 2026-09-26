total=0

for i in range(6):
    units=int(input("enter units used: "))
    if units<=100:
        bill=units*5
        total+=bill
        print(f"bill: ₹{bill}")
        
    elif units<=200 and units>100:
        bill=500+((units-100)*7)
        total+=bill
        print(f"bill: ₹{bill}")

    elif units>200 and units<400:
        bill=500+700+((units-200)*10)
        total+=bill
        print(f"bill: ₹{bill}")

    else:
        bill=500+700+2000+((units-400)*15)
        total+=bill
        print(f"bill: ₹{bill}")


    if bill<1000:
        print("low")
    elif bill>=1000 and bill<=3000:
        print("Medium")
    else:
        print("High")
    print()
    
print()
print(f"total revenue: {total}")
