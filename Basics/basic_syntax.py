# Interacting with the user

# Basic arithmetics
a = 1
b = 2
print(a + b)

# Python follows the C operators order when evaluating mathematical expressions. notice that the power operator is **
print((((1 + 2) * 3) / 4) ** 5)


# Declaring functions
def greeting(name, lastname):
    print("Welcome, " + name + " " + lastname)


# Invoking functions
greeting("joe", "lemon")


# Returning values
def triangle_area(base, height):
    return (base * height) / 2


area_a = triangle_area(5, 4)
area_b = triangle_area(7, 3)
t_sum = area_a + area_b
print("The sum of both areas is: " + str(t_sum))


# Returning several values
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - (hours * 3600)) // 60
    remaining_seconds = seconds - (hours * 3600) - (minutes * 60)
    return hours, minutes, remaining_seconds


# notice we are declaring three variables because we know the function returns three values
hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

# Comparison operators
print(10 > 1)  # will print 'True'
print("Cat" == "Dog")  # will print 'False'
print(1 != 2)  # will print 'True'

# Logic operators
print(10 > 1 and 5 > 7)  # will print 'False'
print(10 > 1 or 5 > 7)  # will print 'True'
print(not(10 > 1 and 5 > 7))  # will print 'True'


# if statements
def hint_username(username):
    if len(username) < 3:
        print("Invalid username")
    else:
        print("Valid username")


hint_username("Yo")  # Will print invalid message
hint_username("Joe")  # Will print valid message


# notice we are returning False without an else block
def is_even(number):
    if number % 2 == 0:
        return True
    return False


print(is_even(10))  # prints 'True'
print(is_even(7))  # prints 'False'


# Nesting if statements with elif
def hint_username_elif(username):
    if len(username) < 3:
        print("Invalid username, must be > 3")
    elif len(username) > 15:
        print("Invalid username, must be < 15")
    else:
        print("Valid username")


hint_username_elif("Yo")  # Will print invalid message
hint_username_elif("Joe")  # Will print valid message
hint_username_elif("John Paul George Ringo")  # Will print invalid message


# Another example
def format_name(first_name, last_name):
    first_name_length = len(first_name)
    last_name_length = len(last_name)
    string = "Name: "
    if first_name_length > 0 and last_name_length > 0:
        string = string + last_name + ", " + first_name
    elif first_name_length > 0 and last_name_length == 0:
        string = string + first_name
    elif first_name_length == 0 and last_name_length > 0:
        string = string + last_name
    else:
        string = ""
    return string


print(format_name("Ernest", "Hemingway"))
print(format_name("", "Madonna"))
print(format_name("Voltaire", ""))
print(format_name("", ""))


# Using loops to control data flow
x = 0
while x < 5:
    print("Not there yet, x= " + str(x))
    x += 1
print("x=" + str(x))


# Return the sum of all the divisors of a number, without including it
def sum_divisors(n):
    total = 0
    divisor = 1
    while divisor < n:
        modulo = n % divisor
        if modulo == 0:
            total += divisor
        divisor += 1
    return total


print(sum_divisors(0))
print(sum_divisors(3))
print(sum_divisors(36))
print(sum_divisors(102))


print("For loops")
for x in range(5):
    print(x)


# Nested for loops
teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)


# Calculate a given number's factorial
def factorial(n):
    r = 1
    for f in range(1, (n+1)):
        r = r * f
    return r


for n in range(0, 10):
    print(n, factorial(n))


# A script that prints the multiples of 7 between 0 and 100, one multiple per line, print only multiples of 7
for number in range(101):
    if (number % 7 == 0 and number != 0) or (number == 0):
        print(number)


# recursion in action
def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0
    # The recursive case is adding this number to
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)


print(sum_positive_numbers(3))  # Should be 6
print(sum_positive_numbers(5))  # Should be 15

for x in range(1, 10, 3):
    print(x)
