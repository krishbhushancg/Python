# Q60. Inverted Triangle
# Print decreasing star rows.

# Test Case
# Input: 4

# Expected Output:
# ****
# ***
# **
# *

n=int(input("enter number: "))

for i in range(n,0,-1):
    for j in range(i+1,1,-1):
        print("*",end="")
    print()