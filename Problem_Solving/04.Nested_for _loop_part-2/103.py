# Q103. Word Pyramid
# Print progressively larger groups of words.

# Test Case
# Input: I love Python code

# Expected Output:
# I
# I love
# I love Python
# I love Python code

n=input("enter sentence: ").upper().split()

for i in range(len(n)):
    for j in range(i+1):
        print(n[j],end=" ")
    print()