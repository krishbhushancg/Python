a=[1,34,67,-78,-1,3,54,7,7]

for i in a:
    if i==0:
        continue
    elif i==-1:
        break
    print(i,end="")
else:
    print("All values processed")