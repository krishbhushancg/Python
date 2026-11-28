n=input("enter string: ")
i=0
total=0

def vowel(n,i,total):
    if i==len(n):
        return total

    if n[i] in "aeiouAEIOU":
        total+=1

    return(vowel(n,i+1,total))



print(vowel(n,i,total))