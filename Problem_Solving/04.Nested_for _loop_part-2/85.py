# Q85. Unique Words
# Print words occurring exactly once.

# Test Case
# Input: this is a test this

# Expected Output: is, a, test

n=input("enter sentence : ").lower().split()

for i in range(len(n)):
    flag=False
    for j in range(len(n)):
        if i!=j and n[i]==n[j]:
            flag=True
            break
    if flag==False:
        print(n[i],end=" ")