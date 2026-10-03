n=int(input("enter number: "))
reverse=0
original=n

while(n>0):
    digit=n%10
    reverse= reverse*10 + digit
    n//=10

print(reverse)

if original==reverse:
    print("number palindrome")
else:
    print("not a number palindrome")

