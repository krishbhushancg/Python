# Q20. Special Coordinate
# Print SPECIAL for i==j, PAIR for i+j==N, otherwise NORMAL. Decide condition priority carefully.

# Test Case
# Input: N=4

# Expected Output: A 4×4 classification grid; diagonal positions are SPECIAL and remaining sum-4 positions are PAIR.


n=int(input("enter number: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print("SPECIAL",end=" ")
        elif i+j==n:
            print("PAIR",end=" ")
        else:
            print("NORMAL",end=" ")
    print()


           