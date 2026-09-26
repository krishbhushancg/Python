#Q19
num=int(input("enter number: "))

if num<0:
    print("Number is negative")
elif num>=0 and num<=10:
    print("Number is between 0 and 10")
elif num>10 and num<=50:
    print("Number is between 10 and 50")
elif num>50 and num<=100:
    print("Number is between 51 and 100")
else :
    print(" Number is above 100")