word = input("enter string: ")

result = filter(lambda ch: ch in "aeiou", word)

print("".join(result))