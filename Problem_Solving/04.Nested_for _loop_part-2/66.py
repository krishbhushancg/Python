# Q66. Hollow Rectangle
# Print only the rectangle boundary.

# Test Case
# Input: rows=4, columns=5

# Expected Output:
# *****
# *   *
# *   *
# *****

n=int(input("enter number of rows: "))
m=int(input("enter number of columns: "))

for i in range(1,n+1):
    for j in range(1,m+1):
        if (i==1 or i==n) or (j==1 or j==m):
            print("*",end="")
        else:
            print(" ",end="")
    print()