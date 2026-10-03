a=input("enter word: ")
digits=0
str2=""

for i in a:
    if i>='0' and i<='9':
        digits+=1
    else:
        str2+=i

print(f"string without digits: {str2}")


