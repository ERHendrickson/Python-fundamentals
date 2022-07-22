"""
multi line 
comments

"""

#inline comment

#use snake case in mulit worded variables (ex. first_name)
#declaring a varible
#boolean
flag = True
#float
grade = 9.45
#int
age = 20
#sting
name = 'ELi'

#console.log in js is = print in js
print(flag)
print( name + " " + str(age) )
print( f"hello there my name is {name}. I am {age} years old." )

print( type( age ) )
print( type( flag ) )

print( len( name ) )

print(name.upper())

grades = [9.8, 8.7, 7.6]

print(grades)
#last index of a list is ALWAYS 1 less than the length

#add an element to a list js - .push(element) : python .append()
grades.append(10.0)
print(grades)
#create a copy of a array
grades_copy = grades[:]
#refrence to a previous array
grades_copy = grades #does not create a copy. changing one will change the other

#object in js are dictionaries in python
student = {
    "name" : "elijah",
    "age" : 20,
    "grade" : 9.6,
    "stack" : "Python/Flask",
    "passed" : True
}

print(student["name"])
first_name = "name"

print(student[first_name])

#add key: value into a dictionary
student["instructor"] = "alfredo salazar"

print(student)

#Tuple
#tuples are immutable (cannot be modified)
course = ("python", "4 weeks", "Elijah Hendrickson")
print(course)

#reasigned the varible. didn't add the value to the variable
course = ("pablo")
print(course)

#conditionals
# > < >= <= == != ! and or not
num = 20
if num > 15:
    print(f"{num} it is greater than 15.") #must be tabbed to fall under conditional
    print("something else")
else:
    print(f"{num} is lesser or equal than 15.")
print("this will always print") #not tabbed so will always execute

"""
order of exe
1. ()
2. * / %
3. + -
4. not
5. < > <= >= ==
"""