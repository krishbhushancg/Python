# Q64. Inverted Pyramid
# Print an inverted number pyramid.

# Test Case
# Input: 4

# Expected Output: A centered pyramid with row widths 7,5,3,1.


n = int(input("Enter number: "))

for i in range(n ,0,-1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(1, 2 * i):
        print(j, end="")

    print()