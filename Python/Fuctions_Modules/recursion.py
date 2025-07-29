# Recursion is programming technique where a fucntion calls itself to solve problem Each recursive call should bring the problem closer to a base case,
# which is a condition that stops the recursion.
# Base Case: The condition under which the function stops calling itself. It prevents infinite recursion.
# Recursive Case: The part where the function calls itself with a simpler or smaller input.

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

print(factorial(5))  


"""
Problem Statement: Directory Size Calculator
You are building a file management tool that needs to calculate the total size of a directory,
including all its nested subdirectories and files.
The directory structure is recursive in nature — a folder can contain files and other folders.
You need to recursively calculate the total size of all files within a directory tree.
"""

import os

def get_directory_size(path):
    total_size = 0
    # List all items in the directory
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        
        if os.path.isfile(item_path):
            # Add file size
            total_size += os.path.getsize(item_path)
        elif os.path.isdir(item_path):
            # Recursively calculate size of the subdirectory
            total_size += get_directory_size(item_path)
    
    return total_size


directory_path = '../'
size_in_bytes = get_directory_size(directory_path)
print(f"Total size: {size_in_bytes / 1024:.2f} KB")
