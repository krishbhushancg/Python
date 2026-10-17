# Q5. Row Number Pattern
# Take N and print the row number N times in each row.

# Test Case
# Input: 4

# Expected Output:
# 1111
# 2222
# 3333
# 4444


n=int(input("enter no. of rows an columns: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end="")
    print()

