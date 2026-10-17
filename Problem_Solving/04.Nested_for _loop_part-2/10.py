# Q10. Alternating 0 and 1
# Take N and print an N×N grid where columns alternate between 0 and 1.

# Test Case
# Input: 4

# Expected Output:
# 0101
# 0101
# 0101
# 0101


n=int(input("enter number: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        if j%2==0:
            print(1,end="")
        else:
            print(0,end="")
    print()
        