#Q14
cp=int(input("enter your cost price: "))
sp=int(input("enter your selling price: "))

loss=(cp-sp)
profit=(sp-cp)
if cp>sp:
    print("there is loss")
    print(f"loss: {loss}")

elif sp>cp:
    print("there is profit")
    print(f"Profit: {profit}")

elif cp==sp:
    print("no loss no profit")