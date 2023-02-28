import re

# look for a string within another string, the r before the string means we are operating
# over a raw string, when usin regexes is advised to use raw strings
result = re.search(r"aza", "plaza")

# <re.Match object; span=(2, 5), match='aza'>, a match object with the position of the found string
print(result)

print(re.search(r"yo", "plaza")) # returns None when does not find any match

# Circumflex(^) tells the machine to look at the beggining of the string
print(re.search(r"^x", "xenon")) # returns a match object (0,1)

# Dot(.) means any character once
print(re.search(r"p.ng", "penguin")) # matches on peng (0,4)
print(re.search(r"p.ng", "sponge")) # matches on pong (1,5)
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE)) # matches on Peng (0,4), notice we are ignoring case

# Wildcards an character classes
# we can define a set of characters using [] and a set of character classes

# Any word starting with P or p
print(re.search(r"[Pp]", "penguin")) # matches on p (0,1)
print(re.search(r"[Pp]", "Python")) # matches on P (0,1)

# Any letter followed by 'way'
print(re.search(r"[a-z]way", "The end of the highway")) # matches on hway (18,22)
print(re.search(r"[a-z]way", "What a way to go")) # returns None, way is preceded by a space

# Find anythin with a letter or a number after 'cloud'
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy")) # matches on cloudy (0,6)
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9")) # matches on cloud9 (0,6)

# Look for any character that is NOT a letter
print(re.search(r"[^a-zA-Z]", "This is a sentence")) # matches on ' ' (4,5)
print(re.search(r"[^a-zA-Z .]", "This is a sentence.")) # Returns none

# We can use a logic or with pipe |
print(re.search(r"cat|dog", "I like cats and dogs")) # matches on cat (7,10)
print(re.findall(r"cat|dog", "I like cats and dogs")) # returns ['cat', 'dog'], notice the find all method

# Repetition qualifiers
# How to match several characters over time

# Look for 'Py' followed by any character, any number of times (including 0), followed by 'n'
print(re.search(r"Py.*n", "Pygmalion")) # matches on Pygmalion (0,9)

# Look for 'Py' followed by any letter, any number of times (including 0), followed by 'n'
print(re.search(r"Py[a-zA-Z]*n", "Python Programming")) # matches on Python (0,6)
print(re.search(r"Py[a-zA-Z]*n", "Pyn")) # matches on Pyn (0,3)

# + matches one or more iterations of the character before it
# look for o any times (with at least one) followed by l any times (with at least one)
print(re.search(r"o+l+", "Gold")) # matches on ol (1,3)
print(re.search(r"o+l+", "Wool")) # matches on ool (1,4)
print(re.search(r"o+l+", "Oil")) # Returns None, it doesn't match the search pattern

# ? means 0 or 1 occurence of the character before it

print(re.search(r"p?each", "To each their own")) # matches on each (3,7), p is 'optional' with p?
print(re.search(r"p?each", "I like peaches")) # matches on peach (7,12)


# To look for special characters (such as . or ?) we use escaping characters, i.e. \
print(re.search(r"\.com", "welcome")) # returns None
print(re.search(r"\.com", "domain.com")) # matches on .com (6,10)

# \w is a shortcut for alphanumeric characters (including letters, numbers, and underscores)
print(re.search(r"[\w] [\w]", "123  Ready Set GO")) # matches
print(re.search(r"[\w] [\w]", "One")) # returns None

# Look for strings that start and end with an 'A'
print(re.search(r"^A.*a$", "Argentina")) # matches Argentina (0,9)
print(re.search(r"^A.*a$", "Azerbaijan")) # returns None

# ex 1
import re
def check_web_address(text):
  pattern = r"^[\w\.\-\+]+\.[a-zA-Z]+$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True
