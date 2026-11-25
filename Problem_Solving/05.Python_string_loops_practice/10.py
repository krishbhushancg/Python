def remover(a,b):
    new=""
    for i in range(len(a)):
        if a[i]==b:
            pass
        else:
            new+=a[i]

    print(f"new string: {new}")

n=input("enter word: ")
m=input("enter character: ")

remover(n,m)

