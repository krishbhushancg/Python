#Q27
hour=int(input("Enter hour: "))
minutes=int(input("Enter minutes: "))
seconds=int(input("Enter seconds: "))

if (0<=hour<=23) and (0<=minutes<=59) and (0<=seconds<=59):
    print("Valid Time")
else:
    print("Invalid Time")