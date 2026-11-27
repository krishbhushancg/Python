# Write countdown(n) that prints every integer from n down to 1, then prints "Done!".

# Constraint: n is a non-negative integer.


a=int(input("enter number: "))
def countdown(n):
    if n==0:
        print("Done!")
        return

    print(n)
    countdown(n-1)


(countdown(a))