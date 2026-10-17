def percentage(marks, total=100):
    if total!=0:
        res=(marks/total)*100
    return(f"{res}%")

n=int(input("enter marks: "))

print(percentage(n))