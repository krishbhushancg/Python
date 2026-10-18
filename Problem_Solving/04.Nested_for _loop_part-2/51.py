# Q51. Prime Numbers Using Nested Loops
# Find all primes from 2 to N.

# Test Case
# Input: 20

# Expected Output:
# 2 3 5 7 11 13 17 19

n=int(input("enter number: "))

for i in range(2,n+1):
    
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")
