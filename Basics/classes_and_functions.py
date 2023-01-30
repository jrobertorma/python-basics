class Apple1:
    pass  # this means there is no code on this block


class Apple:
    color = ""
    flavor = ""


jonagold = Apple()  # we create an instance of a class by calling it like a function
jonagold.color = "red"  # we set the attributes values using dot notation and =
jonagold.flavor = "sweet"
print(jonagold.color)  # red
print(jonagold.flavor)  # sweet


class Piglet:
    name = "piglet"

    # We are defining a method for any instance of the Piglet class
    # notice the self parameter, it represents the instance that the method is executed on
    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))


hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()  # Oink! I'm Hamlet! Oink!


class Person:
    # The constructor
    def __init__(self, name):
        self.name = name

    # A special method to be used when print(Class instance) is called
    def __str__(self):
        return "This person's name is {}".format(self.name)

    # A regular method
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name)


# Create a new instance with a name of your choice
some_person = Person("Joe")

# Call the greeting method
print(some_person.greeting())  # hi, my name is Joe

# Call the __str__ method
print(some_person)  # This person's name is Joe



