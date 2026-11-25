# Q86. Palindrome Word Analyzer
# Check each word for palindrome using character comparisons, not slicing.

# Test Case
# Input: madam level apple

# Expected Output: madam and level are palindromes.


# str=input("Enter a string: ").strip().lower()
# str2=""
# if len(str)==0:
#     print("Enter valid data!!")
# else:
#     length=len(str)
    # for element in range(length-1,-1,-1):
    #     str2=str2+str[element]
    # if str2==str:
    #     print("it is a palindrome")
    # else:
    #     print("not a palindrome")


n=input("enter sentence: ").strip().lower().split()
while len(n)==0:
    n=input("enter sentence: ").strip().lower().split()
palindrome=[]
for i in n:
    new=""
    for j in range(len(i)-1,-1,-1):
        new+=i[j]

    if new==i:
        palindrome.append(i)

for i in palindrome:
    print(i,end=" ")