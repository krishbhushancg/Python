total=0
junior=mid=senior=executive=0
for i in range(8):
    salary=int(input(f"Enter Salary of employee {i+1}: "))
    if salary>100000:
        total+=salary
        executive+=1
        print("Executive")

    elif salary>50000:
        total+=salary
        executive+=1
        print("Senior")

    elif salary>=25000:
        total+=salary
        mid+=1
        print("Mid")

    else:
        total+=salary
        junior+=1
        print("Junior")
    print()
    
    
print(f"number of junior employees: {junior}")
print(f"number of senior employees: {senior}")
print(f"number of executive employees: {executive}")
print(f"number of mid employees: {mid}")

print(f"average salary: ₹{total/8}")