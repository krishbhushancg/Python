# Q1. Sum of Digits at Even Positions

def even_sum(n, pos=1):
    if n == 0:
        return 0

    digit = n % 10

    if pos % 2 == 0:
        return digit + even_sum(n // 10, pos + 1)
    else:
        return even_sum(n // 10, pos + 1)


n = 583246
print(even_sum(n))