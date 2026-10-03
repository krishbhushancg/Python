a=input("enter word: ")
lowercase=0

for i in a:
    if i>='a' and i<='z':
        lowercase+=1

print(f"lowercase letters: {lowercase}")
