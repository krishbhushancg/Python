a=input("enter word: ")
digits=0

for i in a:
    if i>='0' and i<='9':
        digits+=1

print(f"digits: {digits}")
