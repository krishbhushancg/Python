data=(input("enter string: "))

uppercase=0
lowercase=0
digits=0
spaces=0
special_characters=0


for i in data:
    if 'A'<=i and i<='Z':
        uppercase+=1
    elif 'a'<=i and i<='z':
        lowercase+=1
    elif i>='0' and i<='9':
        digits+=1
    elif i==" ":
        spaces+=1
    else:
        special_characters+=1



print(f"number of uppercase letters : {uppercase}")
print(f"number of lowercase letters : {lowercase}")
print(f"number of digits : {digits}")
print(f"number of spaces : {spaces}")
print(f"number of special characters : {special_characters}")


if uppercase>lowercase and uppercase>digits and uppercase>spaces and uppercase>special_characters:
    print(f'uppercase letters has the highest count')
elif lowercase>uppercase and lowercase>digits and lowercase>spaces and lowercase>special_characters:
    print(f'lowercase letters has the highest count')
elif digits>uppercase and digits>lowercase and digits>spaces and digits>special_characters:
    print(f'digits has the highest count')
elif spaces>uppercase and spaces>lowercase and spaces>digits and spaces>special_characters:
    print(f'spaces has the highest count')
elif special_characters>uppercase and special_characters>lowercase and special_characters>digits and special_characters>spaces:
    print(f'special characters has the highest count')
else:
    print("Tie")
