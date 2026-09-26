vowels=0
consonants=0
digits=0
special=0


text=((input("Enter data: ").split()).lower())

for i in text:
    if i ==('a' or i=='e' or i=='i' or i=='o' or i=='u' or 'A' or i=='E' or i=='I' or i=='O' or i=='U'):
        category="vowel"
        vowels+=1

print(f"vowels: {vowels}")
print(f"consonants: {consonants}")
print(f"digits: {digits}")
print(f"special: {special}")
print(f"vowels: {vowels}")