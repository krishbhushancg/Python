n=input("enter a word: ")
a=len(n)

for row in range(len(n)):
    for col in range(row+1):
        print(n[(col)],end=" ")
    print()
for row in range(len(n)-1,0,-1):
    for col in range(row):
        print(n[(col)],end=" ")
    print()