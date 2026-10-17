# Q29. Character Pair Generator
# Print every ordered pair of characters.

# Test Case
# Input: `ABC`

# Expected Output:
# A A
# A B
# A C
# B A
# B B
# B C
# C A
# C B
# C C

n=(input("enter text: "))

for i in n:
    for j in n:
        print(f"{i}{j}")

