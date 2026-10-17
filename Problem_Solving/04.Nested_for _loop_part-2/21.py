# Q21. Character Repetition
# For every character, print it three times.

# Test Case
# Input: `CAT`

# Expected Output:
# CCC
# AAA
# TTT

n=input("enter text: ")

for i in n:
    for j in n:
        print(i,end="")
    print()