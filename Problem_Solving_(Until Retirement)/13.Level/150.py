n=input("enter text: ").split()
longest=0

for i in n:
    if len(i)>longest:
        longest=len(i)

print(longest)