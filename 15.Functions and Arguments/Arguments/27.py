def compare(a, b):
    if a > b:
        return "A is greater", a - b
    elif b > a:
        return "B is greater", b - a
    else:
        return "Equal", 0


print(compare(10, 5))
print(compare(3, 8))
print(compare(5, 5))