print()
print("Press 1 for deposit")
print("Press 2 for withdrawal")
print()

transaction=0
balance=0

for i in range(7):
    task=int(input("enter task number: "))
    if task==1:
        deposit=int(input("enter deposit amount: "))
        balance+=deposit
        print(f"current balance: {balance}")
        transaction+=1

    elif task==2:
        withdrawal=int(input("enter withdrawl amount: "))
        if balance>=withdrawal:
            balance-=withdrawal
            transaction+=1
            print(f"current balance: {balance}")
            if balance<1000:
                print("Low balance")
        else:
            print("insufficient balance")
        
    else:
        print("invalid")
    print()

print(f"final balance: {balance}")
print(f"transaction counts: {transaction}")

