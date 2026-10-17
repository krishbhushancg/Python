def calculate_pay(hours, rate=200, bonus=0):
    return hours * rate + bonus


print(calculate_pay(8))
print(calculate_pay(8, 300))
print(calculate_pay(8, bonus=500))
print(calculate_pay(8, rate=300, bonus=500))