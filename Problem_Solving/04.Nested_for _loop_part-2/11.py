# Q11. Even Number Grid
# Print only even column values for every row.

# Test Case
# Input: rows=3, columns=6

# Expected Output:
# 2 4 6
# 2 4 6
# 2 4 6


n=int(input("enter number of rows: "))
m=int(input("enter number of columns: "))

for i in range(1,n+1):
    for j in range(1,m+1):
        if j%2==0:
            print(j,end=" ")
    print()