print('''1. View profile
2. Edit profile
3. Settings
4. Exit''')

n=int(input("Enter choice: "))

while n<1 or n>4:
    n=int(input("Enter choice: "))


print("Selected option:",n)