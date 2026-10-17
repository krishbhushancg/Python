# Q26. Character Frequency Without count()
# For each character, count its occurrences using nested loops.

# Test Case
# Input: `BANANA`

# Expected Output:
# B = 1
# A = 3
# N = 2

count=0
n=input("enter text:")

for i in n:
    for j in n:
        if i==j:
            count+=1

print(f"count: {count}")