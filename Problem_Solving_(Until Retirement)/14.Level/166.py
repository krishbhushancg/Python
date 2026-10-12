a=[1, 2, 3, 7, 78]
result =True

for i in a:
    if i<0:
        result=False
        break

print(result)