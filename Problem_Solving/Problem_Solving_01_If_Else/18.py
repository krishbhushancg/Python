#Q18
temp=int(input("enter temperature (in celsius): "))

if temp<0:
    print("freezing")
elif temp>=0 and temp<=15:
    print("very cold")
elif temp>15 and temp<=25:
    print("Cold")
elif temp>25 and temp<=35:
    print("Normal")
elif temp>35:
    print("Hot")
