# Q106. Character Frequency Pattern
# Print each character with stars according to frequency.

# Test Case
# Input: BANANA

# Expected Output:
# B *
# A ***
# N **


n=input("enter text: ")


for i in range(len(n)):
    found=0

    for j in range(i):
        if n[i]==n[j]:
            found=1

    if found==0:
        count=0
        for j in n:
            if n[i]==j:
                count+=1

        print(n[i],"*"*count)