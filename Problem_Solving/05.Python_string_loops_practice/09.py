def finder(n,a):
    for i in range(len(n)):
        if n[i]==a:
            print("index:",i)

n=input("enter word: ")
m=input("enter character: ")

finder(n,m)