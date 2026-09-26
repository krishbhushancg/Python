even=0
odd=0
for i in range(5):
    num=input(f"enter number {i+1}: ").split()
    for i in num:
        print(i)
        if len(i)%2==0:
            print("even digits")
            even+=1
        else:
            print("odd digits")
            odd+=1        

if even>odd:
    print("even digits numbers are more")
elif even<odd:
    print("odd digits numbers are more")
else :
    print("odd digits numbers and even digit numbers are equal")
