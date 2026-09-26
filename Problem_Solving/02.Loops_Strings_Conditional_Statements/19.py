text=input("enter sentence: ").split()

digits=0
dot=0
s_char=0
pass_pattern=0
repeated_s_char=0

for word in text:
    a=(word[0:])
    print(F"word: {a}")
    for i in word:
        b=(i)

        if i>='0' and i<='9':
            digits=1
            
        if i=='.':
            dot=1
            
        if i=='@':
            s_char=1
            
        if (i=='_'):
            pass_pattern=1
            
        if i=="_" or i=="@" or i==".":
            repeated_s_char=1
        
    security=digits+s_char+pass_pattern+repeated_s_char+dot

    print(f"security number: {security}")
        
    if security==5:
        print("Safe")
    elif security<5 and security>1:
        print("Review")
    elif security==1:
        print("Suspicious")
