#Q24
price=int(input("enter the price: "))

dis_price=(price-(20/100*price))

if price<500:
   print(f''' original price: {price}
       Discount percentage: 0%
       Discount amount {((0/100*price))}
       Final amount: {(price-(0/100*price))}''')
   
    
elif price>=500 and price<1000:
    print(f''' original price: {price}
    Discount percentage: 5%
    Discount amount {((5/100*price))}
    Final amount: {(price-(5/100*price))}''')

elif price>=1000 and price<2000:
    print(f''' original price: {price}
    Discount percentage: 10%
    Discount amount {((10/100*price))}
    Final amount: {(price-(10/100*price))}''')

elif price>=2000 and price<5000:
    print(f''' original price: {price}
    Discount percentage: 20%
    Discount amount {((15/100*price))}
    Final amount: {(price-(15/100*price))}''')

elif price>=5000:
    print(f''' original price: {price}
    Discount percentage: 20%
    Discount amount {((20/100*price))}
    Final amount: {(price-(20/100*price))}''')