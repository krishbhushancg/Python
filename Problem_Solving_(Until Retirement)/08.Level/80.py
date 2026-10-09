arr=[1,5,3,5,78,546,43,2]
arr1=[]
arr2=[]
for i in range(len(arr)):
    if arr[i]%2!=0:
        arr1.append(arr[i])
    else:
        arr2.append(arr[i])

print(arr1)
print(arr2)