# Q45. Multiplication Triangle
# For row i, print i×1 through i×i.

# Test Case
# Input: 4

# Expected Output: Row 4 contains 4 8 12 16.

n=int(input("enter number: "))

for i in range(1,n+1):
    for j in range(1,n+1): 
        print(i*j,end=" ")
    print()