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
