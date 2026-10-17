def count_digits(number):
    count=0
    while number>0:
        digit=number%10
        count+=1
        number//=10
    return(f"number of digits: {count}")


n=int(input("enter number: "))
print(count_digits(n))
