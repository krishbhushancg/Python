# Q83. Common Words
# Find words occurring in both sentences.

# Test Case
# Input: red blue green / blue yellow red

# Expected Output: red, blue


n=input("enter sentence 1: ").lower().split()
m=input("enter sentence 2: ").lower().split()

for i in n:
    for j in m:
        if i==j:
            print(i,end="")