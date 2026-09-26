# for row in range(5,0,-1):
#     for col in range(row+1,1,-1):
#         print("*",end=" ")
#     print()


n=int(input("enter num: "))
for row in range(n,0,-1):
    for col in range(row):
        print("*",end=" ")
    print()