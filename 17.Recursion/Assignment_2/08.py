# Q8. Decimal to Binary

def binary(n):
    if n == 0:
        return ""

    return binary(n // 2) + str(n % 2)


n = 13

if n == 0:
    print("0")
else:
    print(binary(n))