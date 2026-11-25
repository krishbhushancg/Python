# Q107. Number Triangle With Conditions
# Print E for even, O for odd, and X when row equals column.

# Test Case
# Input: N=4

# Expected Output: Triangle containing E/O with X on the diagonal.

n=int(input("enter number: "))

for i in range(n):
    for j in range(n):
        if i==j:
            print("X",end="")
        elif j%2==0:
            print("E",end="")
        else:
            print("O",end="")
    print()