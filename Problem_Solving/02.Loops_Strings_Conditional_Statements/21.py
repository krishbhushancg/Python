dis=0
dis_amount=0
total=0

dis20=dis15=dis10=0

for i in range(10):
    price=int(input(f"enter price of Product {i+1}: ₹"))
    if price>=5000:
        print("Discount: 20%")
        discount=(0.2*price)
        print(f"Discount amount: ₹{discount}")
        final_amount=(price-(0.2*price))
        print(f"Final amount: ₹{final_amount}")
        dis+=1
        dis20+=1
        total+=discount

    elif price>=3000:
        print("Discount: 15%")
        discount=(0.15*price)
        print(f"Discount amount: ₹{discount}")
        final_amount=(price-(0.15*price))
        print(f"Final amount: ₹{final_amount}")
        dis+=1
        dis15+=1
        total+=discount

    elif price>=1000:
        print("Discount: 10%")
        discount=(0.1*price)
        print(f"Discount amount: ₹{discount}")
        final_amount=(price-(0.1*price))
        print(f"Final amount: ₹{final_amount}")
        dis+=1
        dis10+=1
        total+=discount

    else:
        print("No Discount")
        print(f"Price: {price}")
    print()

print(f"Number of products got discount: {dis}")
print(f"Total Discount: ₹{total}")

print(f"Number of 20% discount items: ₹{dis20}")
print(f"Number of 15% discount items: ₹{dis15}")
print(f"Number of 10% discount items: ₹{dis10}")