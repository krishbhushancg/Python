# Q8. Decreasing Number Grid
# Take N and print 1..N, then one fewer number on every row.

# Test Case
# Input: 4

# Expected Output:
# 1234
# 123
# 12
# 1



n=int(input("enter number: "))

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

