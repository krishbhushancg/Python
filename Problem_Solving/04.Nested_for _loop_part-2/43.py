# Q43. Growing Inner Loop
# For each i from 1 to N, run inner loop 1..i.

# Test Case
# Input: 4

# Expected Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4

n=int(input("enter number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
