def times(min):
    seconds=min*60
    return(f"minutes: {seconds}")

n=int(input("enter minutes: "))

print(times(n))