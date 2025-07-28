#Arguments: Positional, keyword, default, *args, **kwargs.

#1. Positional Arguments - matched by order
def introduce(name, age):
    print(f"My name is {name}, and I am {age} years old.")

introduce("Shruti", 24)


#2  Keyword Arguments -passed using the parameter names
introduce(age=24, name="Shruti")

#3 Default argument - if no value is passed, it take the dafault argument 
def greet(name="Guest"):
    print(f"Hello, {name}")

greet("Shruti")  # Hello, Shruti!
greet()          # Hello, Guest!

# 4 *args: Variable Positional Arguments
#Use *args when you're not sure how many positional arguments you’ll get
def add_all(*numbers):
    print(numbers)       
    return sum(numbers)

print(add_all(1, 2, 3))    

#5 **kwargs: Variable Keyword Arguments
#Use **kwargs to accept any number of keyword arguments.
def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_info(name="Shruti", age=24, city="Pune")


"""
 Problem Statement: Build a Flexible Notification System
 Scenario:
You work at a company where different teams (DevOps, HR, Engineering) need to send notifications via various channels (Email, SMS, Slack). Each team wants different flexibility:

1 Required fields: recipient and message
2 Optional fields: urgency level (default is "normal")
3 Teams want to send multiple messages at once
4 Each team wants to attach metadata like user info, timestamp, etc.

"""


from datetime import datetime

#  main notification function
def send_notification(recipient, urgency="normal", *messages, **metadata):
    print(f"To: {recipient}")
    print(f"Urgency: {urgency}")

    # Handle multiple message lines
    if messages:
        print(" Messages:")
        for msg in messages:
            print(f" - {msg}")
    else:
        print("No messages provided.")

    # Handle extra info
    if metadata:
        print(" Additional Info:")
        for key, value in metadata.items():
            print(f"  {key}: {value}")
    
    print("=" * 50)


# DevOps Team - high urgency with multiple messages
send_notification(
    "devops@company.com",
    "high",
    "Server down!", "Disk space critical!",
    team="DevOps",
    server="prod-server-1"
)

# HR Team - single message using keyword argument, with default urgency
send_notification(
    "hr@company.com",
    message="New HR policy updated.",
    team="HR",
    author="Shruti"
)

# Engineering Team - no message but with metadata
send_notification(
    "eng@company.com",
    sprint="Sprint 42",
    status="In Progress",
    team="Engineering"
)

#  IT Support - default urgency, one message
send_notification(
    "support@company.com",
    "normal",
    "Password reset request received.",
    team="IT Support",
    ticket_id="IT-2025-1001"
)
