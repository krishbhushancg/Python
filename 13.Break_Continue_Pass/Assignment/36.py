a=[3,446,47,-4657,-54,3,6]
b=47
for i in a:
    if i<0:
        continue
    elif i==b:
        print(i,"target found")
        break

else:
    print("target not found")