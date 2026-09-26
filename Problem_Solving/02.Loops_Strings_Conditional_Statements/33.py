code=input("Enter product code: ")

if len(code)==8 and 'A'<=code[:4]<='Z' and '0'<=code[4:]<='9':
    print("Valid Product Code")
else:
    print("Invalid Product Code")
        