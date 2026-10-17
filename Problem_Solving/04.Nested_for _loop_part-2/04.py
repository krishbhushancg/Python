# Q4. Coordinate Grid
# Take rows and columns and print every coordinate.

# Test Case
# Input: rows=2, columns=3

# Expected Output:
# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)

n=int(input("enter no. of rows: "))
m=int(input("enter no. of columns: "))

for i in range(1,n+1):
    for j in range(1,m+1):
        print(f"({i},{j})",end="")
    print()