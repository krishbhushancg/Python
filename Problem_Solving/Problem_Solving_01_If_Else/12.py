#Q12
data=input("Enter : ").strip()

if "A"<=data<="Z" :
    print("Uppercase alphabet")
elif "a"<=data<="z":
    print("Lowercase alphabet")
elif 0<=data<10:
    print("Digit")
else:
    print("Special Character")

