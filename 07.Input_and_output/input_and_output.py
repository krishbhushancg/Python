#Q1
name=input("Enter your name: ")
print(name)

#Q2
city=input("Enter your city: ")
print("Your city is: " + city)

#Q3
name=input("Enter your name: ")
age=input("Enter your age: ")
print("My  name " + name + ", I am " + age + " years old.")

#Q4
answer=("input() function returns a string value")

#Q5
a=input("Enter a number: ")
print(type(a))

#Q6
first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")
print("My name is " + first_name + " " + last_name)

#Q7
name=input("Enter your name: ")
city=input("Enter your city: ")
college=input("Enter your college name: ")
print(f"My name is {name}, I live in {city} and I study in {college}")

#Q8
name1,name2=input("Enter both names: ").split()
print(name1)
print(name2)

#Q9
answer=("the first variable will store 'python' and the second variable will store the value 'programming'")
print(answer)

#Q10
a,b,c=input("Enter three numbers: ").split()
print(a)
print(b)
print(c)

#Q11
a="25"
b=int(a)
print(b,type(b))

#Q12
a="25.5"
b=float(a)
print(b,type(b))

#Q13
a=100
b=str(a)
print(b,type(b))

#Q14
a=int(input("Enter a number: "))
print(a,type(a))

#Q15
a=float(input("Enter a number: "))
print(a,type(a))

#Q16
a = input()
b = input()

print(a + b)        #in this string concatenation is used because both input()  functions return strings a and b so 
                    #the output will be the concatenation of both strings a and b

#Q17
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)

#Q18
name = "Rahul"
age = 20
print(f"My name is {name} and I am {age} years old.")

#Q19
a = 10
b = 20
print(f"The sum of {a} and {b} is {a + b}.")

#Q20
name=input("Enter your name: ")
age=input("Enter your age: ")
print(f"My name is {name} and I am {age} years old.")

#Q21
product_price=float(input("Enter the price of the product: "))
print(f"{product_price:.2f}")

#Q22
answer=(":.2f is used to format the floating-point number to two decimal places.")
print(answer)

#Q23
product_name=input("Enter the product name: ")
price=float(input("Enter the price of the product: "))
quantity=int(input("Enter the quantity of the product: "))
print(f"The product name is {product_name} and its price is {price} and quantity is {quantity} ")

#Q24
print("A", "B", "C")            #it will print a, b and c with space in between them because by default the separator is space

#Q25
print("2026", "08", "19" , sep="-")

#Q26
print("Hello", end=" ")
print("World")

# #Q27
first,second=map(int,input("Enter two numbers: ").split())

print(f"First number: {first}")
print(f"Second number: {second}")
print(f"Sum: {first + second}")

#Q28
price=float(input("Enter the price of the product: "))
quantity=int(input("Enter the quantity of the product: "))

print(f"The price of the product is: {price}")
print(f"The quantity of the product is: {quantity}")
print(f"Total : {price * quantity}")

#Q29
name=input("Enter your name: ")
age=int(input("Enter your age: "))
marks=float(input("Enter your marks: "))

print(f"my name is {name} and i am {age} years old and i scored {marks} in the exam")

#Q30
name=input("Enter your name: ")
age=int(input("enter your age: "))
height=float(input("enter your height: "))
city=input("enter your city name: ")

print(f"My name is {name}, I am {age} years old, my height is {height:.2f} and I live in {city}.")
