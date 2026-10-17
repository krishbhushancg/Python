# Q16. Number Divisibility Grid
# For i,j from 1 to 5, print X if i is divisible by j, otherwise -.

# Test Case
# Input: No input

# Expected Output:
# X - - - -
# X X - - -
# X - X - -
# X X - X -
# X - - - X


# for i in range(1,6):
#     for j in range(1,6):
#         if i==j or j==1 or (j==2 and i==4):
#             print("X",end=" ")
#         else:
#             print("-",end=" ")
#     print()


for i in range(1,6):
    for j in range(1,6):
        if i%j==0:
            print("X",end=" ")
        else:
            print("-",end=" ")
    print()

