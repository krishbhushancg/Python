vowels=0
consonants=0
a=e=ichar=o=u=0

sentence=input("enter your word: ").upper()
for i in sentence:
    if i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        vowels+=1
        if i=='A':
            a+=1
        if i=='E':
            e+=1
        if i=="I":
            ichar+=1
        if i=="O":
            o+=1
        if i=='U':
            u+=1
    else:
        consonants+=1

print(f"number of vowels: {vowels}")
print(f"number of consonants: {consonants}")

if vowels>consonants:
    print("vowels Win")
elif vowels<consonants:
    print("consonants win")
else:
    print("tie")

print(f"a appears {a} times")
print(f"e appears {e} times")
print(f"i appears {ichar} times")
print(f"o appears {o} times")
print(f"u appears {u} times")
