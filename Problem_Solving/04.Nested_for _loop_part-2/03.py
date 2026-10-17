# Q3. Repeated Character Grid
# Take a character, rows and columns. Print the character as a rectangle.

# Test Case
# Input: `*`, rows=3, columns=4

# Expected Output:
# ****
# ****
# ****



n=(input("enter character: "))
m=int(input("enter rows: "))
o=int(input("enter columns: "))

for i in range(m):
    for j in range(o):
        print(n,end="")
    print()