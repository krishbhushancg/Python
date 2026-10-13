while True:
    p = input("Enter password: ")

    if len(p) < 8:
        print("Need at least 8 characters")
    if not any(c.isupper() for c in p):
        print("Need one uppercase letter")
    if not any(c.islower() for c in p):
        print("Need one lowercase letter")
    if not any(c.isdigit() for c in p):
        print("Need one digit")
    if " " in p:
        print("No spaces allowed")

    if (len(p) >= 8 and any(c.isupper() for c in p)
        and any(c.islower() for c in p)
        and any(c.isdigit() for c in p) and " " not in p):
        print("Valid password")
        break