n=int(input("enter a number: "))
prime=True
prime_list=""

if n>1:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print(f"{n} is not prime number")
            prime=False
            break
        else:
            print(f"{n} is a prime number")
            prime_list+=str(i)+", "
else:
    print("not prime number")
    
print(f"prime numbers upto {n} are {prime_list}")