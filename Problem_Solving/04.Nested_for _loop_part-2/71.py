# Q71. Character + ASCII Filter
# Print character pairs whose ASCII difference is greater than 5.

# Test Case
# Input: `ABCDEF`

# Expected Output: Only pairs with difference 6 or more.

s = input("Enter string: ")

for i in s:
    for j in s:
        if ord(j) - ord(i) >= 6:
            print(i, j)


s = input("Enter string: ")

for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if j - i > 5:
            print(s[i], s[j])