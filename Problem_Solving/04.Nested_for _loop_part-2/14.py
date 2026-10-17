# Q14. Equal Coordinate Detector
# For every pair from 1 to 5, print Same when i==j, otherwise Different.

# Test Case
# Input: N=3

# Expected Output:
# Same Different Different
# Different Same Different
# Different Different Same

n=int(input("enter number of rows: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print("Same",end=" ")
        else:
            print("Different",end=" ")
    print()