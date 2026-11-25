# Q104. Reverse Word Pyramid
# Print decreasing groups of words.

# Test Case
# Input: I love Python code

# Expected Output:
# I love Python code
# I love Python
# I love
# I

n=input("enter sentence: ").upper().split()

for i in range(len(n),0,-1):
    for j in range(i):
        print(n[j],end=" ")
    print()