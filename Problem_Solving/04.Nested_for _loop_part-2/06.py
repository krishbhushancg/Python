# Q6. Column Number Pattern
# Take N and print 1 to N in every row.

# Test Case
# Input: 4

# Expected Output:
# 1234
# 1234
# 1234
# 1234


n=int(input("enter no. of rows an columns: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end="")
    print()