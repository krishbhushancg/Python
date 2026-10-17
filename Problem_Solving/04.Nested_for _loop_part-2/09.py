# Q9. Star Rectangle
# Take rows and columns and print a rectangle of *.

# Test Case
# Input: rows=3, columns=5

# Expected Output:
# *****
# *****
# *****

n=int(input("enter number of rows: "))
m=int(input("enter number of columns: "))
for i in range(n):
    for j in range(m):
        print("*",end="")
    print()