# def count(n):
#     if n == 0:
#         return

#     count(n + 1)


#corrected code
def count(n):
    if n == 0:
        return
    print(n)
    count(n - 1)

count(2)

#because it was going in the opposite direction so it could not reach the base case