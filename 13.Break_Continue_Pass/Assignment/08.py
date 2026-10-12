n=input("enter sentence: ").split()
m=input("enter a word: ")

flag=False

for i in n:
    if i==m:
        flag=True
        break

if flag==True:
    print("found")
else:
    print("Not found")
