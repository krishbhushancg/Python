def overlap(a,b):
    count=0
    for i in range(len(a)):
        if b in a:
            count+=1
    print(count)

n=input("enter text: ")
m=input("enter character: ")
overlap(n,m)