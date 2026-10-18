# Q57. Right Triangle
# Print a right triangle of stars.

# Test Case
# Input: 4

# Expected Output:
# *
# **
# ***
# ****

n=int(input("enter number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()