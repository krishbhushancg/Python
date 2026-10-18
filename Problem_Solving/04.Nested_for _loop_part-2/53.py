# Q53. Common Factors
# Find common factors of A and B using nested loops.

# Test Case
# Input: A=12, B=18

# Expected Output:
# 1 2 3 6

n=int(input("enter number: "))
m=int(input("enter number: "))

for i in range(1,n+1):
    if n%i==0:
        for j in range(1,m):
            if m%j==0 and i==j:
                print(j,end=" ")