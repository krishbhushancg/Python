def apply_discount(price, discount=0):
    return price - (price * discount / 100)


price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

print("Final price:", apply_discount(price, discount))