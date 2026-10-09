arr=[1,5,3,5,8,8,8,9,2]
arr1=[]
for i in arr:
    if i not in arr1:
        arr1.append(i)
        
arr1.sort()
print(arr1)
