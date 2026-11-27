def answer(n):
    if n == 0:
        return 0

    n + answer(n - 1)

answer(3)

# here the error is that we are performing arithmetic operations with nonetype value variable