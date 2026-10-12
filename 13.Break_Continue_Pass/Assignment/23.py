a=input("enter text: ").split()
n=input("enter char: ")
flag=False


for i in a:
    if i==n:
        flag=True
        print(i)
        continue
        

if flag==True:
    print("found")
else:
    print("not found")