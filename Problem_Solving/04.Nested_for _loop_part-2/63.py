# Q63. Repeated Number Pyramid
# Print centered repeated row numbers.

# Test Case
# Input: 4

# Expected Output:
#    1
#   222
#  33333

n = int(input("Enter number: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(1, 2 * i):
        print(i, end="")

    print()