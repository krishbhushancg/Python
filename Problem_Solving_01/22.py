#Q22
acc_balance=int(input("Enter account balance: "))
withdrawal_amount=int(input("Enter withdrawal amount: "))

if acc_balance>withdrawal_amount:
    if withdrawal_amount>0:
        if withdrawal_amount%100==0:
            if (acc_balance-withdrawal_amount)>=500:
                print(f'''withdrawl successful 
                Remaining Balance: {(acc_balance-withdrawal_amount)}''')
else:
    print("Withdrawl unsuccessful")
    