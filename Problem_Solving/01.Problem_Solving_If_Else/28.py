#Q28
per_1,age_1=(input("Enter first person name and age: ").split())
per_2,age_2=(input("Enter second person name and age: ").split())
per_3,age_3=(input("Enter third person name and age: ").split())

age_1=int(age_1)
age_2=int(age_2)
age_3=int(age_3)


print(f"{per_1} , {age_1}\n{per_2} , {age_2}\n{per_3} , {age_3}")

if (age_1<age_2) and (age_1<age_3) :
    print(f"{per_1} is the youngest")

elif (age_2<age_1) and (age_2<age_3) :
    print(f"{per_2} is the youngest")

elif (age_3<age_1) and (age_3<age_2) :
    print(f"{per_3} is the youngest")

elif (age_1==age_2) and(age_2==age_3):
    print(f"{per_1} and {per_2} and {per_3} has the same age ")

elif (age_1==age_2):
    print(f"{per_1} and {per_2}have the same age and are the youngest")

elif (age_2==age_3):
    print(f"{per_2} and {per_3} have the same age")

else:
    print(f"{per_1} and {per_3} have the same age")