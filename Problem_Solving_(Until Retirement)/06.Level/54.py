a=[3,7,2,9]
bottom=a[0]
for i in range(len(a)):
    if (a[i]<bottom):
        bottom=a[i]

print(bottom)