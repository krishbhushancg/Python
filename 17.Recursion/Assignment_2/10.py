# Q10. Find Digital Root

def sum_digits(n):
    if n == 0:
        return 0

    return n % 10 + sum_digits(n // 10)


def digital_root(n):
    if n < 10:
        return n

    return digital_root(sum_digits(n))


n = 9875
print(digital_root(n))