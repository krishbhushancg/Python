a=input("enter text: ")
def reverse_text(text):
    if len(text)<=1:
        return text

    return reverse_text(text[1:]) + text[0]

print(reverse_text(a))