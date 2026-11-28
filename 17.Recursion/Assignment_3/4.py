n=int(input("enter number: "))
t=int(input("enter target: "))

count=0

def digit_count(n,t):
    global count

    if n<10:
        return count

    if n%10 == t:
        count+=1

    return(digit_count(n//10,t))

    

print(digit_count(n,t))