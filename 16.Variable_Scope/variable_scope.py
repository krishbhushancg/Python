
# Q1
def show():
    city = "Patna"
    print(city)

show()


# Q2
school = "New Era High School"

def show():
    print(school)

show()


# Q3
if True:
    name = "Krish"

print(name)


# Q4
for i in range(5):
    print(i)

print("Outside loop:", i)



# Q5
# Scope = Where a variable can be accessed in a program.
# Lifetime = How long a variable exists in memory.



# Q6
value = 100

def test():
    value = 200
    print(value)

test()
print(value)


# Q7
clicks = 0

def click():
    global clicks
    clicks += 1

click()
print(clicks)


# Q8
# name = "Asha"

# def show():
#     print(name)
#     name = "Ravi"

# show()
# it will show unbound local error


# Q9
def outer():
    name = "Krish"
    def inner():
        print(name)

    inner()

outer()


# Q10
def create_list():
    numbers = [10, 20, 30]
    return numbers

result = create_list()
result.append(40)

print(result)


# Q11
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner

counter = outer()

print(counter())
print(counter())
print(counter())


# Q12
x = 1

def outer():
    x = 2

    def inner():
        x = 3
        print(x)

    inner()
    print(x)

outer()
print(x)


# Q13
# for i in range(3):
#     print(i)

# print(i)  

# i = 100
# numbers = [i for i in range(3)]

# print(i) 


# Q14
def outer():
    name = "Krish"

    def inner():
        print(name)

    return inner

result = outer()
result()


# Q15
list = [10, 20, 30]
str = "Hello"
sum = 100