a=[[2,4,5],[3,4,6],[3,4,5]]
result=[]

for i in range(len(a)):
    total=0

    for j in range(len(a[i])):
        total+=a[i][j]

    result.append(total)

print(result)