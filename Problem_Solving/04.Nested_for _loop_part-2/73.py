# Q73. Student Marks Matrix
# Input marks for 3 students and 4 subjects; print marks, total and average.

# Test Case
# Input: 80 70 90 60 / 60 75 80 85 / 90 90 95 80

# Expected Output: Student totals 300, 300, 355 and corresponding averages.

n=int(input("enter number of students: "))
m=int(input("enter number of subjects: "))

for i in range(n):
    print(f"marks for student {i+1}")
    total=0
    for j in range(m):
        b=int(input(f"enter subject {j+1} marks: "))
        total+=b
        average=total/m
    print()
    print(f"{total,average}",end=" ")
    print()