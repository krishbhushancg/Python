def palindrome_check(n):
    rev=""
    for i in range(len(n)-1,-1,-1):
        rev+=n[i]
    if n==rev:
        print("palindrome")
    else:
        print("not a palindrome")

n=input("enter word: ")
palindrome_check(n)