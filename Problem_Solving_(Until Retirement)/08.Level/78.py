arr=[2,4,-3,5,-6,7,-4]
arr1=[]
arr2=[]
for i in range(len(arr)):
    if arr[i]>0:
        arr1.append(arr[i])
    elif arr[i]<0:
        arr2.append(arr[i])

print(max(arr1))
print(min(arr2))