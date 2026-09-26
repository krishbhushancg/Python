grade=""
consonants=0
high=0
top=""

for i in range(5):
    name=input(f"enter name of student {i+1}: ").upper
    marks=int(input(f"enter marks of student {i+1}: "))

    vowels=0


    for char in name:
        if char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
            vowels+=1
        else:
            consonants+=1

    if marks>=90 and marks<100:
        grade="A"
    elif marks>=80 and marks<=90:
        grade="B"
    elif marks>=70 and marks<=80:
        grade="C"
    elif marks>=35:
        grade="D"
    else:
        grade="F"

        
    print(f"grade: {grade}")

    if vowels>consonants:
        print("name has more vowels")
    elif vowels<consonants:
        print("name has more consonants")
    else:
        print("name has same number of vowels and consonants")

    print(f"vowels: {vowels}")
    print(len(name))

    if marks>high:
        high=marks
        top=name

print(f"highest: {top},{high}")
