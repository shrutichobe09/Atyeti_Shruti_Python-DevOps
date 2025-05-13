colors=['blue','red','green','pink']

#to iterate to through all item in the list
for color in colors:
    print(color)


#for loop using range()
for i in range(10):
    print(i)

for num in range(1, 6):  # 1 to 5
    print(f"Number: {num}")



numbers = [10, 20, 30, 40]
total = 0

for num in numbers:
    total += num

print(f"Total sum is: {total}")

#while loop
count = 1

while count <= 5:
    print(f"Count is: {count}")
    count += 1  # Increment the counter



correct_password = "shruti@1234"
password = ""

while password != correct_password:
    password = input("Enter the password: ")

print("Access granted!")


#break – Exit the loop early
for number in range(1, 10):
    if number == 5:
        break
    print(number)

#continue – Skip the current iteration
for number in range(1,10):
    if number==5:
        continue
    print(number)

# pass statement is used as a placeholder 
#pass stateement used in empty functions, loops, classes, or conditionals during development
#As a placeholder to avoid syntax errors.
x = 10

if x > 0:
    pass  # add logic here 
else:
    print("x is not positive")


#else clause on loops (for and while). 
#It runs only if the loop completes normally — that is, without hitting a break statement.
numbers = [1, 3, 5, 7, 9]

for num in numbers:
    if num == 4:
        print("Found!")
        break
else:
    print("Not found.")

