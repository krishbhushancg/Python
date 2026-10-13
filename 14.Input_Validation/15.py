n=input("enter username: ").strip()
m=input("enter password: ")

while " " in n or len(n)<5 or len(m)<8 or len(m)==0:
    print("invalid try again")
    n=input("enter username: ").strip()
    m=input("enter password: ")

print("success")

