# Q79. Duplicate Character Detector
# Find characters occurring more than once without count() or set().

# Test Case
# Input: BANANA

# Expected Output: Repeated characters: A, N.


n=input("enter text: ")
repeat=[]
for i in range(len(n)):
    for j in range(i):
        if n[j]==n[i] and n[i] not in repeat:
            repeat.append(n[i])
            break

for i in repeat:
    print(i,end=" ")