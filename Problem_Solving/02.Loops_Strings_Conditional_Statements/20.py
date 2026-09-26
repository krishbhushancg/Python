n=int(input("enter number: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        prod=i*j
        if prod%5==0:
            print(f"{prod} : F",end=" ")
        elif prod%2==0:
            print(f"{prod} : E",end=" ")
        else:
            print(f"{prod} : O",end=" ")
        
    print()