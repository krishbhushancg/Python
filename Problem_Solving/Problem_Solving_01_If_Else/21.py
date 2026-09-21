#Q21
first_side=int(input("enter first side: "))
second_side=int(input("enter second side: "))
third_side=int(input("enter third side: "))

if (first_side+second_side>third_side) and (second_side+third_side>first_side) and (first_side+third_side>second_side):
    print("triangle can be formed")

    if (first_side==second_side==third_side):
        print("triangle is equilateral")

    elif (first_side==second_side) or (second_side==third_side) or (first_side==third_side):
        print("triangle is isoceles")

    else:
        print("triangle is scalene")

else:
    print("triangle cannot be formed")

    print(f"sides: {first_side},{second_side},{third_side}")