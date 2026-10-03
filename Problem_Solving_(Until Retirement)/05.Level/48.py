a=input("enter word: ")
str2=""
vowels=0

for i in a:
    if i =='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vowels+=1
    else:
        str2+=i

print(f"string without vowels: {str2}")