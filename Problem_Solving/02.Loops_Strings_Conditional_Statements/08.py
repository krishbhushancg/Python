budget=0
regular=0
premium=0
luxury=0

amount=0
for i in range(8):
    price=int(input(f"enter price {i+1} : "))
    if price>=5000:
        print("Luxury")
        amount+=price
        luxury+=1
    elif price>=2000 and price<5000:
        print("Premium")
        amount+=price
        premium+=1
    elif price>=500 and price<2000:
        print("Regular")
        amount+=price
        regular+=1
    else:
        print("Budget")
        amount+=price
        budget+=1

print(f"Total Amount: {amount}")
print(f"number of products in Luxury: {luxury}")
print(f"number of products in premium: {premium}")
print(f"number of products in regular: {regular}")
print(f"number of products in budget: {budget}")

average=(amount/8)
print(f"average product price: {average}")
