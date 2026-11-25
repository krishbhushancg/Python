n=int(input("enter number: "))
n=str(n)
def checker(n):
    if "420" in n:
        print("caught")
    else:
        print("escaped")

checker(n)