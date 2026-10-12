def time(hour):
    minutes=hour*60
    return(f"minutes: {minutes}")

n=int(input("enter hours: "))

print(time(n))