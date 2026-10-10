arr=["hi", "hello", "hey" , "jdfnbdf"]
longest=arr[0]
for i in range(len(arr)):
    if len(arr[i])>len(longest):
        longest=arr[i]

print(longest)