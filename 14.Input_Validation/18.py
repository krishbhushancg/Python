n=int(input("enter month: "))
m=int(input("enter day: "))

while n<0 or n>12 or m<0 or m>31:
    n=int(input("enter month: "))
    m=int(input("enter day: "))

print(f"day: {m}")
print(f"month: {n}")