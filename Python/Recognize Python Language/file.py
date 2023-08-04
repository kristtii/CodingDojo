num1 = 42 # integer
num2 = 2.3 # Float
boolean = True # Boolean
string = 'Hello World' # String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary
fruit = ('blueberry', 'strawberry', 'banana') # tuple
print(type(fruit)) # prints <class "tuple">
print(pizza_toppings[1]) # prints Sausage
pizza_toppings.append('Mushrooms') # adds Mushrooms to pizza_toppings
print(person['name']) # Prints John
person['name'] = 'George' # assigns person name to George from John
person['eye_color'] = 'blue' # adds eye color to blue to person
print(fruit[2]) # Prints Banana

if num1 > 45: #if condition
    print("It's greate r") 
else: # else condition
    print("It's lower") #this will be printed in this case

if len(string) < 5:  # if condition
    print("It's a short word!")
elif len(string) > 15: # else if condition
    print("It's a long word!") 
else: #else condition
    print("Just right!")  # this will be printed in this case

for x in range(5): # for loop for(let i = 0; i < 5; i++)
    print(x) # Will print from 0 to 4
for x in range(2,5):  # for loop for(let i = 2; i < 5; i++)
    print(x) # prints 2 3 4
for x in range(2,10,3): # for loop for(let i = 2; i < 10; i+=3)
    print(x) # prints 2 5 8
x = 0 # assigns x equal to 0
while(x < 5): #while lopp looping until x < 5 (4) starting from 0
    print(x) # prints x
    x += 1 # adds 1 to x value

pizza_toppings.pop() # last index will be removed from pizza_toppings
pizza_toppings.pop(1) # index 1 of pizza toppings will be removed from pizzaa toppings 

print(person) # will print: {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color': 'blue'}
person.pop('eye_color') #removes eye color
print(person) # prints {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

for topping in pizza_toppings: # for loop : loops each element of pizza toppings
    if topping == 'Pepperoni': # if condition
        continue # if true do nothing just continue
    print('After 1st if statement') # this will be  printed after first if condition is run (until loop breaks)
    if topping == 'Olives': # another if condition
        break # if true loop will break

def print_hello_ten_times(): # this is a function
    for num in range(10): # for loop from 0 to 10 
        print('Hello') # prints hello 

print_hello_ten_times() # This will print hello 10 times

def print_hello_x_times(x): # same function as above will take range as property
    for num in range(x):
        print('Hello')

print_hello_x_times(4) # prints hello 4 times

def print_hello_x_or_ten_times(x = 10): # this has prop assigned to 10 by default but we can change it. Functions just like 2 previous ones
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #prints hello 10 times
print_hello_x_or_ten_times(4) #prints hello 4 times

"""
Bonus section
"""

print(num3) # num3 is not defined !!! error
num3 = 72 # assing num3 = 72 
fruit[0] = 'cranberry' # tuple cannot be edited !!! Error
print(person['favorite_team']) # there is no favourite_team in person this is error
print(pizza_toppings[7]) # out of bounds !!! Error
print(boolean) # prints true
fruit.append('raspberry') # Tuple cannot be appended !!! Error
fruit.pop(1) # tuple cannot be edited !!! Error