# Q70. Number and Character Grid
# Combine characters from a word with column numbers.

# Test Case
# Input: word=ABCD, N=4

# Expected Output:
# A1 A2 A3 A4
# B1 B2 B3 B4
# C1 C2 C3 C4
# D1 D2 D3 D4

n=int(input("enter number: "))
word=input("enter text: ")

for i in word:
    for j in range(1,n+1):
        print(i,j,end="   ")
    print()