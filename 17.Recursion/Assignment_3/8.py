n=input("enter string: ")

def string_length(s,count=0,n=""):

    if n ==s:
        return count
    return string_length(s,count+1,n+s[count])

print(string_length(n))