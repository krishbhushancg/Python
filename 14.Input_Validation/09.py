n=int(input("enter number: "))

while n<0 or (n%3!=0 or n%5!=0):
    n=int(input("enter number: "))

print("accepted",n)