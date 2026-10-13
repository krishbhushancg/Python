total = 0

for i in range(3):
    score = int(input("Enter score: "))

    while score < 0 or score > 100:
        score = int(input("Enter score between 0 and 100: "))

    total += score

average = total / 3

print("Total:", total)
print("Average:", average)