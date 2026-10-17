def classify_number(number):
    if number>0:
        return("positive")
    elif number<0:
        return("negative")
    else:
        return("zero")


n=int(input("enter number 1: "))

print(classify_number(n))