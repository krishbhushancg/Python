rep=""
count=1

text=input("enter your word: ")
for chr in range(len(text)):
    if chr<len(text)-1 and text[chr]==text[chr+1]:
        count+=1
    else:
        rep+=text[chr]+str(count)
        count=1
print(rep)