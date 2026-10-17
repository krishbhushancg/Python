# Q27. Vowel-Consonant Classification
# Compare each character against AEIOUaeiou using a nested loop.

# Test Case
# Input: `AbC`

# Expected Output:
# A = Vowel
# b = Consonant
# C = Consonant



n=input("enter text: ").lower()

for j in n:
    if j=="a" or j=="e" or j=="i" or j=="o" or j=="u":
        print(j,"= vowel")
    else:
        print(j,"= consonant")