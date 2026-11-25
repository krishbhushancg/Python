# Q87. Longest Palindromic Word
# Find the longest palindrome among words.

# Test Case
# Input: madam level racecar apple

# Expected Output: racecar

n=input("enter sentence: ").strip().lower().split()
while len(n)==0:
    n=input("enter sentence: ").strip().lower().split()

palindrome=[]

for i in n:
    new=""
    for j in range(len(i)-1,-1,-1):
        new+=i[j]

    if new==i:
        palindrome.append(i)

highest=palindrome[0]
for i in palindrome:
    if len(i)>len(highest):
        highest=i

print(f"highest: {highest}")