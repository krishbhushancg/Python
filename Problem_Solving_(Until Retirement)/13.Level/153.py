n=input("enter text: ").lower()
vowel=0

for i in n:
    if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u") :
        vowel+=1

if vowel>0:
    print(True)
else:
    print(False)