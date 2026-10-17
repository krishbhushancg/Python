def format_name(first, last, uppercase=False):

    name=(first+" "+last)
    if uppercase==True:
        return(f"name: {name}").upper()
    else:
        return(f"name: {name}")

n=(input("enter first name: "))
m=(input("enter last name: "))
o=(input("uppercase (yes or no): "))

if o=="yes":
    print(format_name(n,m,True))
else:
    print(format_name(n,m))
