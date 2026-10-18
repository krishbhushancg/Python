# Q56. Pair With Target Sum
# Print all pairs from 1..N whose sum equals target.

# Test Case
# Input: N=5, target=7

# Expected Output:
# 2 5
# 3 4
# 4 3
# 5 2

n=int(input("enter number: "))
limit=int(input("enter target: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==limit:
            print(i,j)