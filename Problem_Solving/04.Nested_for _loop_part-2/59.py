# Q59. Repeated Number Triangle
# Print row number repeated row times.

# Test Case
# Input: 4

# Expected Output:
# 1
# 22
# 333
# 4444

n=int(input("enter number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()