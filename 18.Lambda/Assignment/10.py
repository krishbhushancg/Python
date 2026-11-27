n=int(input("enter price: "))
m=int(input("enter discount percent: "))

calc_discount= lambda a,b: (f"final price: {a-(a*b/100)}")


print(calc_discount(n,m))