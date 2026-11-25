def vowel_check(a):
    vowel=0
    for i in range(len(a)):
        if a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u":
            vowel+=1
    print(f"no. of vowels: {vowel}")

n=input("enter word: ")
vowel_check(n)