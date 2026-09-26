
for i in range(5):
    password=(input(f"enter your password {i+1}: ").strip())

    security=0
    upper=0
    lower=0
    digit=0
    special_character=0

    if len(password)>=8:
        security+=1
        
    for i in password:
        if i>='A' and i<='Z':
            upper=1
        elif i>='a' and i<='z':
            lower=1
        elif i>='0' and i<='9':
            digit=1
        else:
            special_character=1

    security+=upper+lower+digit+special_character
    print(f"security meter: {security}")

    if security==5:
        print(f"strength : Strong")
    elif security>=3:
        print(f"strength : Medium")
    else:
        print(f"strength : Weak")
