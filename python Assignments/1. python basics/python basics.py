#1.Write a program to print your name.
#single line comment
'''
hi this is sahithi
i am currently pursuing bca
'''
"""
This is python programming
"""
print("sahithi")#print my name


#2. Write a program for a Single line comment and multi-line comments

#single line comment
'''
hi this is sahithi
i am currently pursuing bca
'''
"""
This is python programming
"""
print("sahithi")#print my name


#3. Define variables for different Data Types int, Boolean, char, float, double and print on the Console.
# Integer
example_int = 10
print("Integer:", example_int)

# Boolean
example_bool = True
print("Boolean:", example_bool)

# Character 
example_char = 'A'
print("Character:", example_char)

# Float
example_float = 3.14159
print("Float:", example_float)

# Double 
example_double = 2.71828
print("Double:", example_double)

# String 
my_string = "Hello, world!"
print("String:", my_string)


#4. Define the local and Global variables with the same name and print both variables and  understand the scope of the variables.

#Global Variable
my_var="Global variable"
def my_function():
    my_var="Local Variable"
    print(my_var)  #Print local variable
my_function()
print(my_var)

