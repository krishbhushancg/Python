arr = [10, 20, 30]
value = 20

index = -1

for i in range(len(arr)):
    if arr[i] == value:
        index = i
        break

print(index)