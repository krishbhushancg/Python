#Q1
name="krish"
city="patna"
fav_programming_language="Python"
message='python is a beginner friendly language'

print(name)
print(city)
print(fav_programming_language)
print(message)

#Q2
a=""
print(a)
print(len(a))
print(type(a))

#Q3
a="Python Programming"
print(a)
print(len(a))
print(a[0])
print(a[-1])
print(a[2])
print(a[-2])

#Q4
a="Programming"
print(a[0])
print(a[0])
print(a[6])
print(a[-1])

#Q5
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-11])

#Q6
a="krish bhushan"
print(a[1])
print(a[-1])
print(a[7])

#Q7
a="Python Programming"
print(a[0:7])
print(a[7:])
print(a[:])
print(a[0:5])
print(a[-1:-5])

#Q8
a="ABCDEFGHIJKL"
print(a[::2])
print(a[::3])
print(a[1:8:2])
print(a[::-1])

#Q9
a="Python Programming"
print(a[-5:])
print(a[-10:])
print(a[::-2])

#Q10
a="pythonlove"
print(a[:4])
print(a[-3:])
print(a[::2])
print(a[::-1])
print(a[1:-2])

#Q11
a="krish"
b="krish_is_a_bad_boy"
c="he is going for a walk"

print(len(a))
print(len(b))
print(len(c))

#Q12
text = "Python Programming"
print(len(text))
print(text[17])

#Q13
first_name="krish"
last_name="bhushan"
c=(first_name+last_name)
print(c)

#Q14
name="krish "
age=" 18 "
city=" patna "
programming_language=" python"

k=(name+"is 18 years"+age+"old "+"he lives in"+city+"he loves"+programming_language)
print(k)

#Q15
a="krish"
b=89
c=str(b)
print(a+c)

#Q16
a="krish&"
print(a*3)
print(a*5)
print(a*10)

#Q17
a="*"
print(a*10)

#Q18
a="python programming language"
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.swapcase())

#Q19
a="Python" 
b="python"

print(a==b)
c=(a.lower())
d=(b.lower())
print(c==d)

#Q20
a="Python is a programming language"
print("Python" in a)
print("Programming" in a)
print("Java" in a)
print("language" in a)

#Q21
print(a.find("Python"))
print(a.find("programming"))
print(a.find("language"))
print(a.find("Java"))

#Q22
print(a.index("Python"))
print(a.index("programming"))
print(a.index("language"))
# print(a.index("Java"))  it will show error

#Q23
a="banana"
print(a.count("a"))
print(a.count("n"))
print(a.count("b"))


#Q24
filename = "student_notes.pdf"
print(filename.startswith("student"))
print(filename.endswith(".pdf"))
print(filename.startswith(".txt"))

#Q25
text = "I am learning Java"
new_text=(text.replace("Java","python"))
print(new_text)

#Q26
text = "apple apple apple"
new_text=(text.replace("apple","mango"))
print(new_text)

#Q27
new_text2=(text.replace("apple","mango",1))
print(new_text2)

#Q28
text="Python"
b=(text.upper())
print(b)
print(text)
text="PYTHON"
print(text)

#Q29
text = "   Python Programming   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

#Q30
a=(input("Enter your name here:"))
b=(a.strip())
print(b)

#Q31
a="Python is easy to learn"
b=(a.split())
print(b)

#Q32
fruits="apple,banana,mango,orange"
a=(fruits.split(","))
print(a)

#Q33
words = ["Python", "is", "easy"]
a=("".join(words))
print(a)

#Q34
b=("-".join(words))
print(b)
c=("/".join(words))
print(c)


#Q35
name="krish"
age=18
city="patna"

a=(name+" is "+f"{age}"+" "+"he lives in "+city)
print(a)

#Q36
a = 10
b = 20
c=("The sum is "f"{a+b}")
print(c)

#Q37
#A
# text = "Python"
# print(text[20])         #it shows index error    #reason- because the desired index is out of range

#B
# text = "Python"
# text[0] = "J"           #it shows type error      #reason- because string is immutable

#C
# age = 20
# print("Age: " + age)     #it shows type error     #reason- because we cannot add a string and integer value directly

age=20
print("Age: " + str(age))       #correct modifications

#D
# text = "Python"
# print(text.index("Java"))     #it shows value error      #reason- because the desired index is not available in the string

#Q38
a=str(input("Enter your name: ").strip())
c=(a.upper())
d=(a.lower()) 
e=(a.title())
f=(len(a))
g=(a[0])
h=(a[-1])
i=("k" in a)

print(a)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)

#Q39
a=str(input("Enter your sentence: "))
b=len(a)
c=(len(a.split()))
d=(a.upper())
e=(a[0])
f=(a[-1])
g=(a.upper())
h=(a.lower())
i=(a.title())
j=("python" in a)
k=(a.count("p"))

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)



#Q40
a=str(input("First name: ").strip())
b=str(input("Last name: ").strip())
c=str(input("City: ").strip())
d=str(input("Course: ").strip())
e=int(input("Age: ").strip())

g=(a+" "+b)
h=(g.title())
i=(g.lower())
j=(len(g))
k=(g[0])
l=(g[-1])
m=(c+" "+d)
n=(f"{age}")
o=("Python" in d)
p=(d.replace("Python","Java"))
q=(len(d))

print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)
print(n)
print(o)
print(p)
print(q)

