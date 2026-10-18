# Q52. Prime Factor Display
# For every prime up to N, display its factors.

# Test Case
# Input: 10

# Expected Output: 2->1,2; 3->1,3; 5->1,5; 7->1,7.

n=int(input("enter number: "))

for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i, "->", end="")
        print("1", end=",")
        print(i, end="; ")