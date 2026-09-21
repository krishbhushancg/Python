#Q23
username=input("enter your username: ")
if username=="admin":
    password=input("enter your password: ")
    if password=="python123":
        print("Login Successful")
    else:
        print("wrong password")
else:
    print("User not found")