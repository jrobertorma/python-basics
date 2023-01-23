# printing stuff
print("Hello world (from Python)")

# printing stuff with a loop, notice the ':' at the top of the for loop
friends = ['Miguel Angel', 'Rafael', 'Donatelo', 'Leonardo']
for friend in friends:
    print("Yo, " + friend)

# we can also define a range of items, notice we can't concatenate integers to strings directly
for i in range(4):
    print("Item number: " + str(i))

# we also want to have an empty last line
