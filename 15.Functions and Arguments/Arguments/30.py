def order_summary(item, quantity=1, price=100, delivery_fee=40):
    return item, quantity * price + delivery_fee


print(order_summary("Book"))
print(order_summary("Book", 3, 100))
print(order_summary("Book", delivery_fee=20))