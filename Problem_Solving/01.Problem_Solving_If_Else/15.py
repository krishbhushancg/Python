cp=int(input("enter your cost price: "))
sp=int(input("enter your selling price: "))

loss=(cp-sp)
loss_percentage=((cp-sp)/cp*100)

profit=(sp-cp)
profit_percentage=((sp-cp)/cp*100)

if cp>sp:
    print("there is loss")
    print(f"loss: {loss}")
    print(f"loss percent: {loss_percentage}")
elif sp>cp:
    print("there is profit")
    print(f"Profit: {profit}")
    print(f"Profit percent: {profit_percentage}")
elif cp==sp:
    print("no loss no profit")
