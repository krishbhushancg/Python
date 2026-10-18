# Q49. Factors of Every Number
# Print all factors of every number from 1 to N.

# Test Case
# Input: 6

# Expected Output:
# 1 -> 1
# 2 -> 1 2
# 3 -> 1 3
# 4 -> 1 2 4
# 5 -> 1 5
# 6 -> 1 2 3 6


n=int(input("enter nnumber: "))

for i in range(1,n+1):
    print(i,"->",end=" ")
    for j in range(1,i+1):
        if i%j==0:
            print(j,end=" ")
    print()