# for row in range(2,11,2):
#     for col in range(2,row+1,2):
#         print(col,end=" ")
#     print()

# n=int(input("enter num: "))
# for row in range(1,n+1):
#     for col in range(1,row+1):
#         print(2*col,end=" ")
#     print()

n=int(input("enter num: "))
for row in range(n+1):
    for col in range(2*row+2):
        if col%2==0:
            print(col,end=" ")
    print()