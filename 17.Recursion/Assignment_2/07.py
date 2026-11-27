# Q7. Remove All Occurrences

def remove_char(s, ch):
    if len(s) == 0:
        return ""

    if s[0] == ch:
        return remove_char(s[1:], ch)
    else:
        return s[0] + remove_char(s[1:], ch)


s = "mississippi"
ch = "s"

print(remove_char(s, ch))