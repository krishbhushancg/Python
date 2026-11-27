# Write sum_to(n) that returns the sum of all integers from 1 through n.

a=int(input("enter number: "))
sum=0
def sum_to(n):
    if n==0:
        return
    
    global sum
    sum+=n

    sum_to(n-1)
    return(sum)

print(sum_to(a))