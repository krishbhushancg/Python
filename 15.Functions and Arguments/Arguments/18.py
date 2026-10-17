def convert_minutes(minutes, seconds_per_minute=60):
    total_sec=minutes*seconds_per_minute
    return(total_sec)

n=int(input("enter total min: "))

print(convert_minutes(n))