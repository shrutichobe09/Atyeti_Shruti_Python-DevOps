# lambda functions are anonymous functions, meaning they don’t have a name like regular functions defined with def.

#basic lambda function to add numbers
#syntax: lambda argummets: expression
add = lambda x, y: x + y
print(add(3, 5)) 

#lambda with map() - Apply a function to each item in an iterable (list) and return a new iterable.
nums =[1,2,3,4]
squares =list(map(lambda x: x**2, nums))
print(squares)


# Lambda with filter() -  Filter elements in an iterable based on a condition (function returns True or False)
nums = [1,26,78,54,33,21]
evens = list(filter(lambda x: x%2 == 0, nums))
print(evens)

#reduce(function, iterable)-  Repeatedly apply a function to reduce the iterable to a single value.
#must import functools
from functools import reduce
nums = [2,3,4,5,6]
product = reduce(lambda x,y: x*y, nums)
print(product)


"""
problem - you have a list of transaction (in dollars)
you need to 
1. add 18% of tax to each transaction
2. keep only transaction above $100
3. get the total amount

"""
from functools import reduce
transactions = [50, 120, 30, 200, 90]

#1. add 18% of tax to each transaction
with_tax = list(map(lambda x: x * 1.18, transactions))
print("transaction after adding tax", with_tax)

#2. keep only transaction above $100
above_100 = list(filter(lambda x: x>100, with_tax))
print("transaction above $100 ", above_100)

#3. get the total amount
total_amount= reduce(lambda x, y: x + y, above_100)
print("total amount ", total_amount)


"""
Product Discount Pipeline
Problem 2 : A store wants to run a promotion.
Task:

1.Given a list of product dictionaries: { "name": "Item A", "price": 450 }, apply a 15% discount.

2 Filter only items that are still above ₹100 after the discount.

3 Return a list of names of those products.

"""
from pprint import pprint 
products = [
    {"name": "Laptop", "price": 75000},
    {"name": "Mouse", "price": 500},
    {"name": "Keyboard", "price": 1500},
    {"name": "USB Cable", "price": 90},
    {"name": "Monitor", "price": 9500}
]

#1. apply 15% discount to each product
discounted_product = list(map(lambda p: {
    "name": p["name"] ,
   "discounted_price":round(p["price"] * 0.85,2)}, products))
print("prices of product after adding discount of 15% ", discounted_product)

#  2: Filter out products under ₹100
filtered_product = list(filter(lambda p: p["discounted_price"]> 100, discounted_product ))

# Step 3: Extract names of remaining products
final_product_names = list(map(lambda p: p["name"], filtered_product))

pprint(final_product_names)
