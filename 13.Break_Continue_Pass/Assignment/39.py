a=[34,56,35,24,36]

for i in a:
    if i<0:
        continue
    elif i%4==0 and i%6==0:
        print("found:",i)
        break

else:
    print("No matching number")
