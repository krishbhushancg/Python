arr=[1,6,8,2,3]
arr1=[]

if len(arr)>0:
    for i in range(1,len(arr)):
        arr1.append(arr[i])

arr1.append(arr[0])

print(arr1)