def create_email(username, domain="@example.com"):
    email=username+domain
    return(f"email-Id: {email}")


n=(input("enter name: "))


print(create_email(n))
