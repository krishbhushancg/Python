# Write fibonacci(n) that returns the nth Fibonacci number using these definitions:


a=int(input("enter number: "))
def fibonacci(n):
    if n<=1:
        return n

    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(a-1))
