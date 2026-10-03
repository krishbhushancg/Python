str=input("enter word:").strip()
str1=""

for i in range(len(str)-1,-1,-1):
    str1+=str[i]

if str==str1:
    print("mirror compatible")
else:
    print("not mirror compatible")


