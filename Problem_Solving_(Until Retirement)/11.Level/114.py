def vote(age):
    if age>=18:
        return(True)
    else:
        return(False)

n=int(input("enter age: "))

print(vote(n))