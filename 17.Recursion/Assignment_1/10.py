# Write power(base, exponent) that returns base raised to exponent.


a=int(input("enter base: "))
b=int(input("enter power: "))
def power(a, n):
    if n == 0:
        return 1

    return a * power(a, n - 1)

print(power(a, b))