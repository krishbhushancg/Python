# Q30. Different Character Pairs
# Print ordered pairs whose positions are different.

# Test Case
# Input: `ABC`

# Expected Output: A B, A C, B A, B C, C A, C B.


n=(input("enter text: "))

for i in n:
    for j in n:
        if i!=j:
            print(f"{i}{j},",end=" ")