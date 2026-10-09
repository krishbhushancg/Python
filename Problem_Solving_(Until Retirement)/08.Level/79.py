arr=[0, 1, 0, 1, 1]
zero=0
one=0

for i in range(len(arr)):
    if arr[i]==0:
        zero+=1
    else:
        one+=1

print(f"zero: {zero}")
print(f"one: {one}")