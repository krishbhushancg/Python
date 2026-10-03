print("A = absent")
print("P = Present")
p=0
a=0

for i in range(5):
    print()
    for j in range(7):
        att=input(f"enter P or A for Student {j+1}: ").upper()
        if att=="P":
            p+=1
        else:
            a+=1

print(f"present: {p}")
print(f"absent: {a}")
