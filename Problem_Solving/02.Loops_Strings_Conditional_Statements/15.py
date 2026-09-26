even=0
odd=0
positive=0
negative=0
zero=0

largest=0

matrix=int(input("no. of rows: "))
for i in range(matrix*matrix):
    num=int(input(f"enter elements {i+1}: "))

    if num>0:
        positive+=1
    if num<0:
        negative+=1
    if num==0:
        zero+=1
    if num%2==0:
        even+=1
    if num%2!=0:
        odd+=1
    if largest==0 or largest<num:
        largest=num
    else:
        largest=largest

print(f"positive: {positive}")
print(f"negative: {negative}")
print(f"even: {even}")
print(f"odd: {odd}")
print(f"zero: {zero}")
print(f"largest: {largest}")

