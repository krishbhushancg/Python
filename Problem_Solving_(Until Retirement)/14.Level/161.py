a=[1, -2, 0, 5, -3]
positive=0
negative=0
zero=0

for i in a:
    if i>0:
        positive+=1
    elif i<0:
        negative+=1
    else:
        zero+=1

print(zero)
print(positive)
print(negative)