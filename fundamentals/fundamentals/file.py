num1 = 42 #variable declaration type number
num2 = 2.3 #variable declaration type float
boolean = True #var dec data type boolean
string = 'Hello World' #var dec type string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #initialize type list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #initialize type dicitonary
fruit = ('blueberry', 'strawberry', 'banana') # initialize type tuple
print(type(fruit)) # log statement type check tuple
print(pizza_toppings[1]) # log state access value
pizza_toppings.append('Mushrooms') #add value to list
print(person['name']) #log statement access value
person['name'] = 'George' #change value/add value
person['eye_color'] = 'blue' #change/add value
print(fruit[2]) #log statement access value

if num1 > 45: #conditional if
    print("It's greater") #log statement
else: # conditional else
    print("It's lower") # log statement

if len(string) < 5: # if conditional length check  
    print("It's a short word!") #log statement
elif len(string) > 15: #elif conditional length check
    print("It's a long word!") #log statement 
else: #else conditional
    print("Just right!") #log statement

for x in range(5): #for loop start: 0 stop 5 increment: 1
    print(x) #log statement
for x in range(2,5): #for loop start: 2 stop: 5 increment: 1
    print(x) # log statement
for x in range(2,10,3): #for loop start: 2 stop: 10: increment: 3
    print(x) #log statement
x = 0 #var declaration
while(x < 5): #while loop start 0: stop 4
    print(x) #log statement
    x += 1 #var increments 1

pizza_toppings.pop() #list delete last value
pizza_toppings.pop(1) # list delete value at index 1

print(person) #log statement dictionary person
person.pop('eye_color') #delete value 'eye_color' from dictionary 
print(person) #log statement dictionary person

for topping in pizza_toppings: #for loop values in list pizza_toppings
    if topping == 'Pepperoni': #if conditional boolean check
        continue #continue do nothing
    print('After 1st if statement') #log statement
    if topping == 'Olives': #if conditional boolean check
        break #ends loop if true

def print_hello_ten_times(): #function declaration
    for num in range(10): #for loop start: 0 end: 9: increment 1
        print('Hello') #log statement string 'Hello'

print_hello_ten_times() #function invoked log statement 'Hello' x10

def print_hello_x_times(x): #function declaration: param: x
    for num in range(x): #for loop: start 0: end x - 1: increment 1
        print('Hello') # log statement: string'hello'

print_hello_x_times(4) #function invoked: argument 4: log statement 'Hello' x4

def print_hello_x_or_ten_times(x = 10): #function invoked: parameter 10 if no argument passed: 
    for num in range(x): #for loop: start 0: end: x or 10 if x is not given: increment 1
        print('Hello') #log statement string 'Hello'

print_hello_x_or_ten_times() #function invoked: no argument given -> defaults to 10 log statement 'Hello' x10
print_hello_x_or_ten_times(4) #function invoked: argemnt 4 log statement 'Hello' x4


"""
Bonus section
"""

# print(num3) # variable undefined name error
# num3 = 72  # variable dec
# fruit[0] = 'cranberry' # tuple object does not supp item assign Type error
# print(person['favorite_team']) #keyError no key in dictionary
# print(pizza_toppings[7]) #list index out of range
#   print(boolean) # indentation error : unexpected indent
# fruit.append('raspberry') # attribute error'tuple' object has no attribute append
# fruit.pop(1) # attribut error 'tuple' object has no attribute pop