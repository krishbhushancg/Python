n=input("enter string: ")

flag=False
i=-1
new=""

def palindrome(n):
    global flag
    global i
    global new

    if i==-len(n)-1:
        return flag

    new+=n[i]
    i-=1

    if len(n)==len(new):
        if n==new:
            flag=True
    

    return(palindrome(n))


print(palindrome(n))