# Q62. Number Pyramid
# Print centered odd-length number sequences.

# Test Case
# Input: 4

# Expected Output:
#    1
#   123
#  12345
# 1234567


n = int(input("Enter number: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(1, 2 * i):
        print(j, end="")

    print()