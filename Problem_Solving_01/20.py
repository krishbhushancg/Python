#Q20
first_side=int(input("enter first side: "))
second_side=int(input("enter second side: "))
third_side=int(input("enter third side: "))

if (first_side+second_side>third_side) and (second_side+third_side>first_side) and (first_side+third_side>second_side):
    print("triangle can be formed")