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

#increment number
count = 0
def increment():
    global count
    count += 1

increment()
print(count) 


# nonlocal Keyword (for nested functions)- Used to modify a variable in the enclosing (non-global) scope.
def outer():
    x="outer"
    def inner():
        nonlocal x
        x="inner"
    inner()
    print(x)

outer()


"""
problem- 
You're building a visitor counter for a website. The counter keeps track of the total number of visitors.
Additionally, each time a visitor is counted, a local welcome message is generated inside a function.

1 Use a global variable to keep count of total visitors.
2 Inside a function, increment the visitor count and generate a local message like Welcome, Visitor #X.
3 Print both the welcome message (local) and the updated visitor count (global).
4 Call the function multiple times to simulate multiple visitors.
"""

visitor_count = 0  # Global variable
def visit():
    global visitor_count
    visitor_count += 1
    message =" Welcome visitor"
    print(message)

visit()
visit()
visit()
visit()
print("Total visitors:", visitor_count)


"""
Problem Statement 2: Task Tracker

1 Keep a global variable total_tasks to store the total number of tasks added so far.
2 Define a function add_task(task_name):
   - Inside the function, increase the global task count.
   - Create a local variable message with the format: "Task added: <task_name> (Task #<total_tasks>)".
   - Print the local message.
3 After adding some tasks, print the total number of tasks added (from the global variable).

"""
total_task =0

def add_task(task_name):
    global total_task
    total_task +=1
    message = f"Task added: {task_name}, toatal task {total_task}"
    print(message)

add_task("write report")
add_task("attend meeting")
add_task("code review")
print("toatl task added today ", total_task)