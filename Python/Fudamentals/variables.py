#Variables are containers for storing data values
#variable is name that is assigned to value

#store integer value
x = 5

# store string value
name = "shruti" 
company_name= "Atyeti" 

print(x)
print(name)
print(company_name)

#rules for naming variable
"""
- variable can contain only letters and digit,underscore
- vaiable names are case-sensitive
- variable name cannot start with digit , we can start with underscore and letters
- keywords cannot be used as variable name 
"""

#valid example
age = 21
_colour = "black "
total_score = 80

"""
#invalid example
1name = "Error"  # Starts with a digit
class = 10      # 'class' is a reserved keyword
user-name = "chobe-shruti"  # hyphen is not allowed 

"""

#Dynamic Typing
#Python variables are dynamically typed,meaning the same variable can hold different types of values during execution
x=9
x="nine"
print(x)

#Multiple Assignments
#python allows multiple variable to be assigned in single line 
a=b=c=50
print(a,b,c)

#Assigning Different Values
age, salary = 23, 56000
print(age,salary)


#Scope of a Variable
#There are two methods how we define scope of a variable in python which are local and global.

#Variables defined inside a function are local variable
def local_variable():
    my_name="i am local variable"

local_variable()

#Global Variables:
#Variables defined outside any function are global and can be accessed inside functions using the global keyword.
a = "I am global variable"

def global_variable():
    global a
    a = "Modified globally"
    print(a)

print(global_variable())
print(a)
print('dghhhfjj')