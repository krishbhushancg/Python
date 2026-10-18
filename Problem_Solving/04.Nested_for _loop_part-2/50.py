# Q50. Perfect Number Detector
# Find perfect numbers up to N using divisor sums.

# Test Case
# Input: 30

# Expected Output:
# Perfect: 6, 28



n=int(input("enter number: "))

print("Perfect:", end=" ")

for i in range(1,n+1):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum+=j
    if sum==i:
        print(f"{i}",end=" ")


