arr=[1,2,3,4,5]
sum=0


for i in range(len(arr)):
    sum+=arr[i]

avg=sum/len(arr)

count=0
for i in range(len(arr)):
    if arr[i]>avg:
        count+=1

print(count)