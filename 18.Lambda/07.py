n=input("enter character: ")

is_vowel = lambda ch : 'Vowel' if ch in 'aeiouAEIOU' else 'No Vowel'

print(is_vowel(n))