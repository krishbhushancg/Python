for row in range(0,5):
    alpha = ""
    for col in range(0,row + 1):
        alpha += chr(65 + row) + " "  
    print(alpha)

for i in range(1,6):
    for j in range(i):
        print(chr(64+i),end=" ")
    print()