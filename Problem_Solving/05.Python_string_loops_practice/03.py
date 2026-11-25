
# def p_check(n):
#     flag1=False
#     str1=n[0:(len(n)//2)]
#     str1r=""
#     for i in range((len(n)//2)-1,-1,-1):
#         str1r+=n[i]
#     print(str1r)
#     if str1==str1r:
#         flag1=True
    
    
#     print()

#     flag2=False
#     str2=n[len(n)//2:]
#     str2r=""
#     for j in range(len(n)-1,(len(n)//2)-1,-1):
#         str2r+=n[j]
#     print(str2r)
#     if str2==str2r:
#         flag2=True

#     if flag1 and flag2:
#         print("yes")
#     else:
#         print("no")


# k=input("enter text: ").lower().strip()
# p_check(k)



n=(input("enter word: ")).lower().strip()

str1=n[0:len(n)//2]
str2=n[len(n)//2:]

def p_check(a):
    flag=False
    org=a
    rev=""
    for i in range(len(a)-1,-1,-1):
        rev+=a[i]
    if org==rev:
        flag=True
        print(org)

    if flag==True:
        print("half equal")
    print()

p_check(str1)
p_check(str2)
