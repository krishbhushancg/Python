# Q41. Word Length Difference
# Print each pair and absolute difference of their lengths.

# Test Case
# Input: `I love Python code`

# Expected Output: Every ordered pair with its length difference.

n=input("enter text: ").split()

for i in n:
    for j in n:
        print(i,j,":",abs(len(i)-len(j)))