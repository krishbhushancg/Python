# Q2. Multiplication Pair
# Take N and print the multiplication result for every pair from 1 to N.

# Test Case
# Input: 3

# Expected Output:
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9

n=int(input("enter number: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        print(f"{i} X {j} = {i*j}")
