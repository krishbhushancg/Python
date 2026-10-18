# Q54. Common Multiples
# Generate multiples and print common multiples up to a limit.

# Test Case
# Input: A=6, B=8, limit=30

# Expected Output: No common multiple below 30 except 24.

n=int(input("enter number: "))
m=int(input("enter number: "))
limit=int(input("enter limit: "))

for i in range(n,limit,n):
    for j in range(m,limit,m):
            if i==j:
                print(j)

