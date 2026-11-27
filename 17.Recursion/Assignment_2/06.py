# Q6. Check Prime Number

def is_prime(n, divisor=2):
    if divisor * divisor > n:
        return True

    if n % divisor == 0:
        return False

    return is_prime(n, divisor + 1)


n = 29
print(is_prime(n))