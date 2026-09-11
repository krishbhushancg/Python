word =input("Enter your word: ").lower()

count = 0

for character in word:
    if character == "a":
        count = count + 1

print("Count of a:", count)