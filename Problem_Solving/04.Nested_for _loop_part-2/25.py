# Q25. Count Matching Characters
# Count equal character comparisons between two strings without using count().

# Test Case
# Input: `ABC` and `BCD`

# Expected Output:
# 2

count=0
n=input("enter text:")
m=input("enter text:")

for i in n:
    for j in m:
        if i==j:
            count+=1

print(f"count: {count}")