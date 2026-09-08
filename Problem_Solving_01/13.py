#Q13
data=input("Enter : ").strip()
if "A"<=data<="Z"  or "a"<=data<="z":
    print("It's an alphabet")

    if data=="A" or data=="E" or data=="I" or data=="O" or data=="U" or data=="a" or data=="e" or data=="i" or data=="o" or data=="u" :
        print("Vowel")
    else:
        print("it's a consonant")

else:
    print("invalid data")

