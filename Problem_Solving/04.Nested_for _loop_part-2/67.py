# Q67. Hollow Triangle
# Print a hollow right triangle.

# Test Case
# Input: 5

# Expected Output:
# *
# **
# * *
# *  *
# *****

n=int(input("enter number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        if (i==1 or i==j or j==1 or i==5) :
            print("*",end="")
        else:
            print(" ",end="")
    print()