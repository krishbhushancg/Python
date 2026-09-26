excellent=0
good=0
passed=0
fail=0


for i in range(10):
    marks=int(input("enter marks:"))
    if marks<=100 and marks>=75:
        print("Excellent")
        excellent+=1
    elif marks>=50 and marks<75:
        print("good")
        good+=1
    elif marks>=35 and marks<50:
        print("pass")
        passed+=1
    elif marks<35:
        print("fail")
        fail+=1
    else:
        print("invalid data")

print(f"number of students in excellent category: {excellent}")
print(f"number of students in good category: {good}")
print(f"number of students in passed category: {passed}")
print(f"number of students in fail category: {fail}")

