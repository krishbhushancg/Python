a=[12,45,3,35,65,436,39]
n=35
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