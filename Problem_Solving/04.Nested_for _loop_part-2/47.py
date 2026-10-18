# Q47. Dynamic Range Based on Input
# For i=0..N-1, run range(i).

# Test Case
# Input: 4

# Expected Output: i=0 produces no inner output; later rows show 0, then 0 1, then 0 1 2.

n=int(input("enter number: "))

for i in range(0,n):
    for j in range(i):
        print(j,end=" ")
    print()