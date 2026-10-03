a=input("enter word: ").lower().strip()
b=""
for i in range(len(a)-1,-1,-1):
    b+=a[i]

if a==b:
    print("palindrome")
else:
    print("not palindrome")

