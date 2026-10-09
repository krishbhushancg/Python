arr=[2,5,3,7,9,1,4]
arr1=[3,5,3,6,78,1]
arr2=[]
for i in range(len(arr)):
    for j in range(len(arr1)):
        if arr[i]==arr[j]:
            arr2.append(arr[i] or arr[j])
            
print(arr2)