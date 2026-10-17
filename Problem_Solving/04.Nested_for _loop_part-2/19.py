# Q19. Pair Product Filter
# Print pairs and products only when the product is even.

# Test Case
# Input: N=3

# Expected Output:
# 1 2 2
# 2 1 2
# 2 2 4
# 2 3 6
# 3 2 6

n=int(input("enter number: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        if (i*j)%2==0:
            print(i,j,i*j)