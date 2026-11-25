# Q89. Most Repeated Character
# Find the highest-frequency character without count/max/set.

# Test Case
# Input: BANANA

# Expected Output: A

n=input("enter text 1: ")
m=input("enter text 2: ")

same=[]
for i in n:
    for j in m:
        if i==j and i not in same:
            same.append(i)

highest=same[0]
for i in same:
    print(i,end="")