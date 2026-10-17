# Q24. Character Matching
# Compare every character of two strings and print equal pairs.

# Test Case
# Input: `ABC` and `BCD`

# Expected Output:
# B B
# C C

n=input("enter text:")
m=input("enter text:")

for i in n:
    for j in m:
        if i==j:
            print(i,j,end="")
    print()

