# Q9. Check Only Digits

def only_digits(s):
    if len(s) == 0:
        return True

    if s[0] < '0' or s[0] > '9':
        return False

    return only_digits(s[1:])


s = "50291"
print(only_digits(s))