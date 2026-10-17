# Q12. Odd Number Grid
# Print odd numbers from 1 to N in every row.

# Test Case
# Input: N=7

# Expected Output:
# 1 3 5 7
# 1 3 5 7
# 1 3 5 7
# 1 3 5 7
# 1 3 5 7
# 1 3 5 7
# 1 3 5 7


n=int(input("enter number of rows: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        if j%2!=0:
            print(j,end=" ")
    print()