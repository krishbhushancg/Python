# Q77. Ticket Price Grid
# Odd seats cost 100; even seats cost 150.

# Test Case
# Input: rows=2, seats=5

# Expected Output:
# 100 150 100 150 100
# 100 150 100 150 100

n=int(input("enter number of rows: "))
m=int(input("enter number of seats: "))

for i in range(1,n+1):
    for j in range(1,m+1):
        if j%2==0:
            print(150,end=" ")
        else:
            print(100,end=" ")
    print()