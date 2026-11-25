# Q84. Duplicate Words
# Find repeated words in a sentence without count().

# Test Case
# Input: this is a test this

# Expected Output: this

n=input("enter sentence : ").lower().split()
rep=[]
for i in range(len(n)):
    for j in range(i):
        if n[i]==n[j] and n[j] not in rep:
            rep.append(n[j])
            break

for i in rep:
    print(i,end="")
