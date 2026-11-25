# Q109. Student Performance Matrix
# Analyze marks for N students and M subjects: totals, averages, highs, pass/fail and extremes.

# Test Case
# Input: 3 students × 3 subjects: 80 70 90 / 60 75 80 / 90 90 95

# Expected Output: Complete report; Student 3 has highest total 275.

n=int(input("enter number of students: "))
m=int(input("enter number of subjects: "))
highest=0

for i in range(n):
    print(f"marks for student {i+1}")
    total=0

    
    for j in range(m):
        a=int(input("enter marks: "))
        while a<0 or a>100:
            print("enter valid marks")
            a=int(input("enter marks: "))
        total+=a
        average=total/m
    print(f"average: {average}")
    percentage=((total/(100*m))*100)
    if percentage>=90 and percentage<100:
        print("grade: A")
    elif percentage>=80:
        print("grade: B")
    elif percentage>=60:
        print("grade: C")
    elif percentage>=40:
        print("grade: D")
    elif percentage>=35:
        print("Pass")
    else:
        print("Fail")
    print()
    if total>highest:
        highest=total
        first=f"student{i+1}"


print(f"highest total: {highest}")
print(f"{first} has highest total")



        
