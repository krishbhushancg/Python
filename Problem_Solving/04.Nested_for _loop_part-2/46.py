# Q46. Conditional Dynamic Loop
# Run inner loop i times and print only even inner values.

# Test Case
# Input: 4

# Expected Output:
# 2
# 2
# 2 4
# 2 4 6

n=int(input("enter number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        if j%2==0:
            print(j,end=" ")
    print()