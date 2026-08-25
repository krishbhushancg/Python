#Q1

a=20
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#Q2

a=4
b=2.2

print(a+b)
print(type(a+b))


print(a-b)
print(type(a-b))


print(a*b)
print(type(a*b))


print(a/b)
print(type(a/b))


print(a//b)
print(type(a//b))


print(a%b)
print(type(a%b))


print(a**b)
print(type(a**b))



#Q3

english=90
maths=98
physics=99

number_of_subjects=3

total_marks=(english+maths+physics)
average_marks=((english+maths+physics)/number_of_subjects)

print(total_marks)
print(average_marks)



#Q4

product_price=450
quantity=78

total_price=(product_price*quantity)

print(total_price)

#Q5
number=78
solution=(number%2)  #if the answer is 0 then the number is divisible by 2
print(solution)


#Q6
c=78
d=3
print(c/d)
print(c//d)

e=-98
f=-2
print(e/f)
print(e//f)


#Q7

a=-95
b=-90
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)


#Q8

a=9
b=-6

print(a-a)   #positive-positive
print(a-b)   #positive-negative
print(b-a)   #negative-positive
print(b-b)   #negative-negative


#Q9
a=9
b=-3

print(a/a)
print(b/a)
print(a/b)
print(b/b)


#Q10
a=90
b=-45

print(a%a)
print(b%a)
print(a%b)
print(b%b)

#Q11
print(10 + 5 * 2)           #multiplication(*)
print(20 - 4 / 2)           #division(/)
print(10 + 20 / 5 * 2)      #division(/)
print(2 + 3 * 4 ** 2)       #exponentiation(**)
print(100 - 20 // 5)        #floor division(//)

#Q12
a1=(10 + 5 * 2)
a2=((10 + 5) * 2) 
print(a1)
print(a2)      # both the operations have different results as parentheses has the highest priority due to which python calculates the parenthesis value first and hence the value changes


b1=(20 - 10 / 2)
b2=((20 - 10) / 2)
print(b1)
print(b2)       # both the operations have different results as parentheses has the highest priority due to which python calculates the parenthesis value first and hence the value changes


c1=(2 + 3 * 4)
c2=((2 + 3) * 4)
print(c1)
print(c2)       # both the operations have different results as parentheses has the highest priority due to which python calculates the parenthesis value first and hence the value changes


#Q13
a=True
b=False

print(a+b)
print(type(a+b))


print(a-b)
print(type(a-b))


print(a*b)
print(type(a*b))


print(b/a)
print(type(b/a))


print(b//a)
print(type(b//a))


print(b%a)
print(type(b%a))


print(a**b)
print(type(a**b))


#Q14
print(True + 5)
print(False + 5)
print(True * 10)            #when doing mathematical calculation on python on boolean values , it takes True =1 and False=0
print(False * 10)
print(True - 5)
print(False - 5)


#Q15
a="Krish"
b="Bhushan"
c=(a+b)

print(c)

#Q16
a="extreme"
print(a*3)


#Q17
a="trace"
b="back"

print(a+b)              #only string concatenation works here
# print(a-b)           #subtraction , multiplication and division doesn't work on mathematical operations with string
# print(a*b)
# print(a/b)

#Q18
value=None
x=7
# None - 5
# None * 5
# None / 5
# None // 5
# None % 5
# None ** 5             #all raise a TypeError

#none represents the absence of a value hence arithmetic operations are not supported with none.

#Q19
a=7
b=0

# c=(a/b)
# print(c)   it will show ZeroDivisionError

d="first"
e="second"
# f=(d*e)      it will show TypeError: can't multiply sequence by non-int of type 'str'     
# print(f)

g=None
h=2
# i=(g*h)
# print(i)       it will show TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'


#Q20
a=75
b=7
addition=(a+b)
subtraction=(a-b)
multiplication=(a*b)
division=(a/b)
floor_division=(a//b)
modulus=(a%b)
exponentiation=(a**b)

print("Addition:",(addition))
print("Subtraction:",(subtraction))
print("Multiplication:",(multiplication))
print("Division:",(division))
print("Floor Division:",(floor_division))
print("Modulus:",(modulus))
print("Exponentiation:",(exponentiation))

#Q21
a = 10
b = -3
c = 2.5

print(a+b+c)            # 9.5
print(a+b-c)            #4.5
print(a/b/c)            #-1.333---
print(a*b*c)            #-75.0
print(a//b//c)          #-2.0
print(a%b%c)            #0.5
print(a**b+c)           #2.501
print((a+b)+c-b*a)      #39.5
print((b-a)+a*3+8//2)   #21
print(a+b**6+c//3+20)   #759..0




































