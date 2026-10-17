# Q18. Pair Sum Filter
# Print all pairs from 1 to N whose sum is greater than N.

# Test Case
# Input: N=4

# Expected Output:
# 1 4
# 2 3
# 2 4
# 3 2
# 3 3
# 3 4
# 4 1
# 4 2
# 4 3
# 4 4


n=int(input("enter number: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j>n:
            print(i,j)