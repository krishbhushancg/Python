# Q75. Attendance Checker
# Input P/A for each student/day and count present/absent.

# Test Case
# Input: 2 students × 4 days: P A P P / A P A P

# Expected Output: Student 1 Present=3 Absent=1; Student 2 Present=2 Absent=2.

n=int(input("enter number of students: "))
m=int(input("enter number of days: "))


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
    print(f"student {i+1}  present: {present}  absent: {absent}")