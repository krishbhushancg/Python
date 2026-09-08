#Q7
num=int(input("Enter number: "))
if (num%3==0) and (num%7==0):
    print(f"{num} is divisible by 3 and 7")
elif (num%3!=0) and (num%7==0):
    print(f"{num} is divisible by 7")
elif (num%3==0) and (num%7!=0):
    print(f"{num} is divisible by 3")
else:
    print(f"{num} is not divisible by 3 and 7")