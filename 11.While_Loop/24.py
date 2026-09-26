n=input("enter string: ").lower()
a=0
i=0
while i<=len(n)-1:
    if n[i]=='a':
        a+=1
    i+=1

print(f"a appears {a} times")