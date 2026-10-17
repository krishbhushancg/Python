# Q22. Character with Position
# For every character, print it with repetition numbers 0,1,2.

# Test Case
# Input: `AB`

# Expected Output:
# A 0
# A 1
# A 2
# B 0
# B 1
# B 2


n=input("enter text: ")

for i in n:
    for j in range(3):
        print(i,j)
    