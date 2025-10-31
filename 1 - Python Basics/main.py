# Variables in python
a = 100
name = 'Anand Mansabdar'

# Declaring and assigning variables
age = 20
height = 5.7
is_Student = True

# Printing variables
print(f'Variable : {a},Name : {name},Age: {age},height: {height}, IsStudent: {is_Student}')

# Variable naming convention :- should be descriptive, starts with letter or an _, can contain numbers, letters and underscores, case sensitive

# Valid variable names
first_name = 'Anand'
last_name = 'Mansabdar'

# Invalid variable names
# 2age = 21
# first-name = "anand"

# variable types
# Python is a dynamically typed lang, type of a variable is detemined at runtime
age = 20 #int
name = 'Anand' # str
isWorking = False # bool

# Type checking
print(type(age))
print(type(name))
print(type(isWorking))

# Type conversion
age_str = str(age)
print(age_str)
print(type(age_str))

# int -> str
# str(number only) -> int
# int <-> float

# Dynamic Typing :- Python allows the type of a variable to change as the program executes
var = 10
print(var, type(var))

var = 'Hello'
print(var, type(var))

var = 3.14
print(var, type(var))
