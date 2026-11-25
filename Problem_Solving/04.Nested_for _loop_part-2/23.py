# Q23. Compare Every Character
# Compare every character with every other character and label Same/Different.

# Test Case
# Input: `AB`

# Expected Output: A/A is Same; all other ordered pairs are Different.


n=input("enter text:")
repeat=""
for i in n:
    for j in n:
        if i==j and j not in repeat:
            repeat+=j
            print(f"{i}/{j} is same",end=" ")
        elif i!=j:
            print(f"{i}/{j} is different",end=" ")
    print()

