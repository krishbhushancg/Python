# Q65. Diamond Pattern
# Print a star diamond.

# Test Case
# Input: 4

# Expected Output:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

n = int(input("Enter number: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(1, 2 * i):
        print("*", end="")
    print()
for i in range(n-1,0,-1):
    
    for j in range(n - i):
        print(" ", end="")
    
    for j in range(1, 2 * i):
        print("*", end="")
    
    print()