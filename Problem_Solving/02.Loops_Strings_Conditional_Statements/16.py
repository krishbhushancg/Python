uppercase=0
lowercase=0
digits=0
special_characters=0

password=input("enter password: ")
for i in password:
    if i>='A' and i<='Z':
        uppercase+=1
    elif i>='a' and i<='z':
        lowercase+=1
    elif i>='0' and i<='9':
        digits+=1
    else:
        special_characters+=1


t=len(password)


print(f"uppercase characters: {uppercase}   percentage: {(uppercase/t)*100}")
print(f"lowercase characters: {lowercase}   percentage: {(lowercase/t)*100}")
print(f"digits: {digits}   percentage: {(digits/t)*100}")
print(f"special characters: {special_characters}   percentage: {(special_characters/t)*100}")

if uppercase>lowercase and uppercase>digits and uppercase>special_characters:
    print(f'uppercase letters has the highest count')
elif lowercase>uppercase and lowercase>digits and lowercase>special_characters:
    print(f'lowercase letters has the highest count')
elif digits>uppercase and digits>lowercase and digits>special_characters:
    print(f'digits has the highest count')
elif special_characters>uppercase and special_characters>lowercase and special_characters>digits:
    print(f'special characters has the highest count')
else:
    print("Tie")



