digits=0
underscores=0
invalid_special_characters=0
strength=0

for i in range(5):
    user=input((("enter username: ").strip()).lower())
    
    print(f"length: {len(user)}")
    print(f"first character: {user[0]}")

    for i in user:
        if i>='0' and i<='9':
            digits+=1
        elif i=="_":
            underscores+=1
        elif not(i>='a' and i<='z'):
            invalid_special_characters=1


    print(f"number of underscores: {underscores}")
    print(f"number of digits: {digits}")


    if invalid_special_characters==1:
        print("invalid")
    elif invalid_special_characters==0 and digits>1 and underscores>=1:
        print("Valid")
    elif underscores<1 or digits<1:
        print("Needs improvement")

    