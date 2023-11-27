# Part 1: Write User's Name to a File
name = input("Enter your name: ")
with open('name.txt', 'w') as file:
    file.write(name)

# Part 2: Read and Print Name from File
with open('name.txt', 'r') as file:
    name_read = file.read()
print(f"Your name is {name_read}")

# Part 3: Read First Two Numbers from a File and Print Their Sum
with open('numbers.txt', 'r') as file:
    number1 = int(file.readline())
    number2 = int(file.readline())
print(f"The sum of the first two numbers is: {number1 + number2}")

# Part 4: Print Total of All Numbers in a File
total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        total += int(line)
print(f"The total sum of all numbers is: {total}")
