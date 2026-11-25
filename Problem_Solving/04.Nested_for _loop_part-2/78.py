# Q78. Classroom Attendance Summary
# Print each student's P/A totals and the highest-attendance student.

# Test Case
# Input: same as Q75

# Expected Output: Student 1 has highest attendance.

n=int(input("enter number of students: "))
m=int(input("enter number of days: "))

highest=0
student=0

for i in range(n):
    print(f"attendance for student {i+1}")
    absent=0
    present=0
    
    for j in range(m):
        att=input("enter P/A: ").lower()

        while att!="p" and att!="a":
            print("try again")
            att=input("enter P/A: ").lower()
        if att=="a":
            absent+=1
        else:
            present+=1
        print("Present:", present)
        print("Absent:", absent)
        print()

        if present > highest:
            highest = present
            student = i + 1

print(f"Student {student} has highest attendance.")