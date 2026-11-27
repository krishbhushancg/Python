# Q4. Count a Character

def count_char(s, ch):
    if len(s) == 0:
        return 0

    if s[0] == ch:
        return 1 + count_char(s[1:], ch)
    else:
        return count_char(s[1:], ch)


s = "programming"
ch = "m"

print(count_char(s, ch))