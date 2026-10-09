arr=[1,6,8,2,3]
arr1=[]

if len(arr)>0:
    arr1.append(arr[-1])

for i in range(len(arr)-1):
    arr1.append(arr[i])

print(arr1)