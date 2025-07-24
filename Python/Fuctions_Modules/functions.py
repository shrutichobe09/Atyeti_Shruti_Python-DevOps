#functions are blocks of reusable code that performs a specific task 

def greet(name):
    return f"Hello, {name}, Good morning "

print(greet("shruti"))

#building calculator app using function 
def add(a,b):
    return a+b

def sub(a, b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

print(add(10,5))
print(sub(20,14))
print(multiplication(20,4))
print(division(35,7))


#use case - log monitoring  system
"""
problem statement-  you're building a log monitoring tool. Logs are received from different services
in this format:

[ERROR] Disk space low on server1
[INFO] Backup completed on server2
[WARNING] High memory usage on server3

You need to write a system using functions to:

1. Parse the log lines

2. Count the number of messages by type (ERROR, WARNING, INFO)

3. Identify and return the most frequent error message

4. Support future reuse for different types of logs (e.g., from DB, API, etc.)

"""
from collections import defaultdict

#extract log level and message
def parse_log_line(line):
    if not line.startswith('[') or ']' not in line:
        return None, None
    level = line.split(']')[0][1:]
    message = line.split(']')[1].strip()
    return level, message


#Counts number of each log type.
def count_log_types(log_lines):
    counts = defaultdict(int)
    for line in log_lines:
        level, _ = parse_log_line(line)
        if level:
            counts[level] += 1
    return dict(counts)

#find most repeated error message 
def most_frequent_error(log_lines):
    error_counts = defaultdict(int)
    for line in log_lines:
        level, message = parse_log_line(line)
        if level == "ERROR":
            error_counts[message] += 1
    if error_counts:
        return max(error_counts, key=error_counts.get)
    return None

logs = [
    "[ERROR] Disk space low on server1",
    "[INFO] Backup completed on server2",
    "[WARNING] High memory usage on server3",
    "[ERROR] Disk space low on server1",
    "[ERROR] CPU temperature high on server2",
    "[INFO] User login on server1",
    "[ERROR] Disk space low on server1",
    "[ERROR] Disk space low on server1",
    "[WARNING] High memory usage on server3",
    "[WARNING] High memory usage on server3"

]


print(count_log_types(logs))
print(most_frequent_error(logs))