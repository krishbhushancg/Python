# for row in range(1,10,2):
#     for col in range(1,row+1,2):
#         print(col,end=" ")
#     print()

# n=int(input("enter num: "))
# for row in range(0,n+1):
#     for col in range(0,row+1):
#         print(2*col+1,end=" ")
#     print()

n=int(input("enter num: "))
for row in range(n+1):
    for col in range(2*row+2):
        if col%2!=0:
            print(col,end=" ")
    print()



# n=int(input("enter num: "))

# for row in range(1,n+2,2):
#     for col in range(1,row+1,2):
#         print(col,end=" ")
#     print()