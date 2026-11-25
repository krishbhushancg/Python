def d_checker(n):
    digit=0
    for i in range(len(n)):
        if n[i]>='0' and n[i]<='9':
            digit+=1
    print(f"number of digits: {digit}")


n=input("enter text: ")
d_checker(n)