# Write count_up(n) that prints numbers from 1 through n in ascending order.

a=int(input("enter number: "))
def countup(n):
    if n==0:
        return

    countup(n-1)
    print(n)

countup(a)