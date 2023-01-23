# Using string indexing
name = "John"
print(name[0])  # prints 'J'

# Using negative indexes
text = "This is a looooong string hahaha"
print(text[-1])  # prints 'a'

# Getting a substring
greeting = "Hello world (again)"
print(greeting[1:4])  # prints world (again)
print(greeting[6:(len(greeting))])  # prints world (again)
print(greeting[:5])  # prints Hello
print(greeting[6:])  # prints world (again)

greeting_new = "Hello world (again)"
print(greeting_new.index("Hello"))  # prints 0

# Checking if a substring is in a given string
pets = "Cats & Dogs"
print("Dragons" in pets)  # prints False
print("Cats" in pets)  # prints True

upper_string = "HELLO!"
print(upper_string.lower())  # prints 'hello!'


spaces_string = " hello "
print(spaces_string.strip())  # prints 'hello'
print(spaces_string.lstrip())  # prints 'hello '
print(spaces_string.rstrip())  # prints ' hello'


# String methods
methods_string = "This is a test string"
print(methods_string.count("is"))  # prints '2'
print(methods_string.endswith("string"))  # prints 'True'
print(methods_string.endswith("yo"))  # prints 'False'
print(methods_string.isnumeric())  # prints 'False'
split_string = methods_string.split()
print(split_string[0])  # prints 'This'
joined_string = " ".join(split_string)
print(joined_string)  # prints 'This is a test string'

name_m = "Paul"
l_number = len(name_m) * 3
print("Hello {name}, your lucky number is: {number}".format(name=name_m, number=l_number))  # prints: 'Hello Paul, your lucky number is: 12'

price = 7.5
with_tax = price * 1.15
print("Base price: ${:.2f}, With Tax: ${:.2f}".format(price, with_tax))  # notice the :.2f, this means we are going to format a float number with two decimals


def to_celcius(x):
    return (x-32)*5/9


for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celcius(x)))  # prints a formatted temperature conversions table,
    # notice the {:>3} placeholder, this means that it will leace 3 spaces before printing the formatterd variable


# List examples
x = ["Now", "we", "are", "cooking!"]
type(x)  # prints <class, list>
print(x)  # prints ['Now', 'we', 'are', 'cooking!']
len(x)  # prints 4
print("are" in x)  # prints True
print("today" in x)  # prints False
print(x[0])  # prints Now


fruits = ["Pineapple", "Apple", "Banana", "Melon"]
fruits.append("Kiwi")
print(fruits)  # ['Pineapple', 'Apple', 'Banana', 'Melon', 'Kiwi']
fruits.insert(0, "Orange")  # inserts at index 0 (the beginning of the list)
print(fruits)  # ['Orange', 'Pineapple', 'Apple', 'Banana', 'Melon', 'Kiwi']
fruits.remove("Melon")  # removes the first occurrence
print(fruits)  # ['Orange', 'Pineapple', 'Apple', 'Banana', 'Kiwi']
fruits.pop(3)  # removes the given index element of the list
print(fruits)  # ['Orange', 'Pineapple', 'Apple', 'Kiwi']
fruits[2] = "Strawberry"  # reassigns/overwrites the given index element of the list
print(fruits)  # ['Orange', 'Pineapple', 'Strawberry', 'Kiwi']

winners = ["Ashely", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))

# Prints al the multiples of 3 between 0 and 100 using list comprehension
z = [x for x in range(0, 101) if x % 3 == 0]
print(z)

