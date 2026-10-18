# Q61. Right-Aligned Triangle
# Print a right-aligned star triangle.

# Test Case
# Input: 4

# Expected Output:
#    *
#   **
#  ***
# ****

n=int(input("enter number: "))

for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    print()