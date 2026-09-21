#Q22
print(-10%3)
acc_balance=int(input("Enter account balance: "))
withdrawal_amount=int(input("Enter withdrawal amount: "))

if withdrawal_amount>0:
    if withdrawal_amount%100==0:
        if acc_balance>=withdrawal_amount:
            if (acc_balance-withdrawal_amount)>=500:
                print(f'''withdrawl successful 
                Remaining Balance: {(acc_balance-withdrawal_amount)}''')
            else:
                print("Withdrawal unsuccessful")
                print("At least ₹500 must remain")
        else:
            print("Withdrawal unsuccessful")
            print("Insufficient balance")
    else:
        print("Withdrawal unsuccessful")
        print("Amount must be divisible by 100")
else:
    print("Withdrawl unsuccessful")

