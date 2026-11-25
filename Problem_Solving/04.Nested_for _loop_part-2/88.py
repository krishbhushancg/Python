# Q88. Maximum Common Character
# Find the character with the highest matching frequency between two strings.

# Test Case
# Input: ABCA / BCAD

# Expected Output: B or C according to the defined matching-frequency rule; explain tie handling.

n=input("enter text 1: ")
m=input("enter text 2: ")

same=[]
for i in n:
    for j in m:
        if i==j and i not in same:
            same+=i
for i in same:
    print(i,end="")
