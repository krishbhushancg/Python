#Q6
num=int(input("Enter number: "))
if (num%5==0) and (num%11==0):
    print(f"{num} is divisible by 5 and 11")
elif (num%5!=0) and (num%11==0):
    print(f"{num} is divisible by 11")
elif (num%5==0) and (num%11!=0):
    print(f"{num} is divisible by 5")
else:
    print(f"{num} is not divisible by 5 and 11")