while True:
    print('''1. Check balance
2. Deposit money
3. Withdraw money
4. Exit''')

    balance=10000

    n=int(input("enter operation number: "))

    while n<0 or n>4:
        print("try again")
        n=int(input("enter operation number: "))

    if n==1:
        print(f"Showing balance: {balance}")

    elif n==2:
        deposit=int(input("enter deposit amount : "))
        while deposit<0:
            deposit=int(input("enter deposit amount : "))
        balance+=deposit
        print(f"current balance: {balance}")
    elif n==3:
        withdraw=int(input("enter deposit amount : "))
        while withdraw<0 or withdraw>balance:
            withdraw=int(input("enter withdrawal amount : "))
        balance-=withdraw
        print(f"current balance: {balance}")

    elif n==4:
        print("exiting...")
        break

