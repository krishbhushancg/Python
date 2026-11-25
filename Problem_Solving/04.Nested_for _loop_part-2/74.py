# Q74. Multiplication Table Matrix
# Print tables 1..N, each from ×1 to ×10.

# Test Case
# Input: N=3

# Expected Output: Tables for 1, 2 and 3 through ×10.

n=int(input("enter number: "))

for i in range(1,n+1):
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")
    print()