# Q44. Shrinking Inner Loop
# Decrease the inner-loop size each row.

# Test Case
# Input: 4

# Expected Output:
# 1 2 3 4
# 1 2 3
# 1 2
# 1


n=int(input("enter number: "))

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()