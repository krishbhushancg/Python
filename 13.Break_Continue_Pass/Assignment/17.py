a=input("enter word: ").lower()
vowel=0
consonant=0

for i in a:
    if i=="a" or i=="e"or i=="i" or i=="o" or i=="u":
        vowel+=1
    else:
        consonant+=1

print(consonant)