text=input("enter sentence: ").upper().split()

vowels=0
consonants=0


for word in text:
    a=(word[0:])
    print(F"word: {a}")
    for char in word:
        b=(char)
        if char=="A" or char=="E" or char=="I" or char=="O" or char=="U":
            vowels+=1
        else:
            consonants+=1

    if vowels>consonants:
        print("status: vowel heavy")
    elif vowels<consonants:
        print("status: consonant Heavy")
    else:
        print("status: balanced")
    print()