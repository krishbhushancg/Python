# Q105. Word Length Pattern
# Print stars equal to each word's length.

# Test Case
# Input: I love Python

# Expected Output:
# I *
# love ****
# Python ******


m=input("enter sentence: ").split()

for i in range(len(m)):
    print(m[i],(len(m[i])*"*"))