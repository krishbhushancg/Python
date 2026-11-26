a=int(input("enter number: "))
count=0
def count_digits(n):
    global count
    if n<=0:
        return 1
    
    count_digits(n//10)
    global count
    count+=1

    return count

print(count_digits(a))

