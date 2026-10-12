s = input("Enter a string: ")

for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            print(s[i])
            break
    else:
        continue
    break
else:
    print("No repeated character")


