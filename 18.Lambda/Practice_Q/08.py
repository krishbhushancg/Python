word = input("enter string: ")

result = map(lambda ch: ch.upper(), word)

print("".join(result))