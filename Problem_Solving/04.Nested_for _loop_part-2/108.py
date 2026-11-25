# Q108. Multiplication Pattern Challenge
# Replace multiples of 3 with X, 5 with Y, both with Z.

# Test Case
# Input: N=5

# Expected Output: 3 and 6 positions become X; 5 becomes Y; 15 becomes Z where applicable.

n=int(input("enter number: "))

for j in range(1,n+1):
        if j%3==0 and j%5==0:
            print("z",end=" ")
        elif j%3==0:
            print("x",end=" ")
        elif j%5==0:
            print("y",end=" ")
        else:
            print(j,end=" ")