n=input("enter word: ")
a=input("enter character: ")

def counter(n,a):
    count=0
    for i in n:
        if i==a:
            count+=1
    print(f"{a} appeared {count} times")


counter(n,a)