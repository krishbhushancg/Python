def count_digits(number):
    count=0
    if number>0:
        while number>0:
            digit=number%10
            count+=1
            number//=10
        return(f"number of digits: {count}")
    else:
        a=str(number)
        return(f"number of digits: {len(a)-1}")

def is_even(number):
    if(number%2==0):
        return("even")
    else:
        return("not even")


def absolute(number):
    if number<0:
        return(-(number))
    else:
        return(number)


def analyze_number(number):
    return(count_digits(number),is_even(number),absolute(number))

n=int(input("enter number: "))
print(analyze_number(n))