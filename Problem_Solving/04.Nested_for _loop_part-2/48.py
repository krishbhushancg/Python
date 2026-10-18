# Q48. Reverse Dynamic Range
# For each i, print i down to 1.

# Test Case
# Input: 4

# Expected Output:
# 1
# 2 1
# 3 2 1
# 4 3 2 1

n=int(input("enter number: "))

for i in range(1,n+1):
    for j in range(i+1,i+1):
        print(j,end=" ")
    print()