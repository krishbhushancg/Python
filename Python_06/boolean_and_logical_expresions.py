#Q22
age=25
print(age>=18)
print(age<=60)
print(age>=18 and age<=60)

#Q23
age=16
print(age<18 or age>60)        #first it will calculate the first condition (age < 18) and give result true
                                #and then second condition (age > 60) and give the result false
                                #then it will give the final result true

#Q24
age=20
print(not(age<18))          #first it will calculate the condition (age < 18) and give result false
                            #then it will give the final result true

#Q25
age=20
a=(age>10 and age<50)
print(a)

#Q26
age=69
a=(age<10 or age>100)
print(a)

#Q27
age=69
a=(not(age<39 and age>60))
print(a)

#Q28
#0 is a falsy value
#1 is a truthy value
#-5 is a truthy value
#"" is a falsy value
#False is a falsy value
#True is a truthy value
#None is a falsy value

#Q29
print(bool(0))
print(bool(10))
print(bool(""))
print(bool("hello"))
print(bool(None))

#Q30

print(bool(0))
print(type(0))

print(bool(1))
print(type(1))  

print(bool(""))
print(type(""))

print(bool(False))
print(type(False))

print(bool(None))
print(type(None))
