def show_square():
    print("****")
    print("****")
    print("****")
    print("****")

show_square()

print()

def show_square2():
    for i in range(4):
        for j in range(4):
            print("*", end="")
        print()

show_square2()

print()

n=int(input("enter number: "))
def show_square3():
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

show_square3()