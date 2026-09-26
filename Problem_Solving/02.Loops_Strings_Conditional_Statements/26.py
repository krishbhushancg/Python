poor=average=good=excellent=outstanding=0
total=0

for i in range(10):
    rating=float(input("Enter your rating: "))
    if rating>9 and rating<=10:
        total+=rating
        outstanding+=1
        print("Outstandiing")

    elif rating>7 and rating<=9:
        total+=rating
        excellent+=1
        print("Excellent")

    elif rating>5 and rating<=7:
        total+=rating
        good+=1
        print("Good")

    elif rating>3 and rating<=5:
        total+=rating
        average+=1
        print("Average")

    elif rating>0 and rating<=3:
        total+=rating
        poor+=1
        print("Poor")

    else:
        print("Invalid")
        

print(f"number of poor movies: {poor}")
print(f"number of average movies: {average}")
print(f"number of good movies: {good}")
print(f"number of excellent movies: {excellent}")
print(f"number of outstanding movies: {outstanding}")

print(f"average rating:  {total/10}")

