word=input("enter word: ").lower()
vowel=0

for i in word:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vowel+=1

print(f"vowel: {vowel}")