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


