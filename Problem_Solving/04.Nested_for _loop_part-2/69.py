# Q69. Diagonal Cross
# Print * on both diagonals.

# Test Case
# Input: 5

# Expected Output:
# *   *
#  * *
#   *
#  * *
# *   *

n=int(input("enter number: "))

for i in range(n):
    for j in range(n):
        if ((j==n-i-1) or (i==j)):
            print("*",end="")
        else:
            print(" ",end="")
    print()