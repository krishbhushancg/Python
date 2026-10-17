# Q7. Increasing Number Grid
# Take N and print 1, then 12, then 123, and so on.

# Test Case
# Input: 4

# Expected Output:
# 1
# 12
# 123
# 1234


n=int(input("enter number: "))

for i in range(1,n+1):
    for j in range(1, i+1):
        print(j,end="")
    print()