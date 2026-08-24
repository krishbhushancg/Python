#Q24
student_name="krish"
student_age=17
student_height_in_cm=175
is_krish_a_student=True
student_result=None

print(student_name,student_age,student_height_in_cm,is_krish_a_student,student_result)

#Q25
a=50
b=50.0
c="50"

print(type(a),type(b),type(c))

#Q26
a=True
b="True"

print(type(a),type(b))    # here variable a has an boolean value whereas variable b has an string value as it is written under double quotes

#Q27
a=None
b="None"

print(type(a),type(b))   #here variable a has an none type value whereas variable b has an string value as it is written under double quotes

#Q28
value=69
print(type(value))

value="39"           # reassigned the variable value as string
print(type(value))   #now the value assigned to it is a string , previously it was int

#Q29
product_name="Kawasaki"
product_quantity=69
product_price=89.8
Product_availability=False
product_discount_information=None

print(type(product_name),type(product_quantity),type(product_price),type(Product_availability),type(product_discount_information))

#Q30
a=10            #int
print(type(a))  


b=10.0          #float        
print(type(b))    


c="10"          #string
print(type(c))
print("here we have variables a , b and c but the value inside a is a int type , whereas in b the value is in double quotes so it is considered as a string value and in c we have our value is in decimal so it is considered as a float type")



d=True          #boolean
print(type(d))  



e="True"        #string
print(type(e))
print("here we have variables d , e  but the value inside d is a boolean type , whereas in e the value is in double quotes so it is considered as a string value ")



f=None          #nonetype
print(type(f))


g="None"        #string
print(type(g))
print("here we have variables f , g  but the value inside f is a boolean type , whereas in g the value is in double quotes so it is considered as a string value ")
