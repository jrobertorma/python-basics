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

# Capturing groups are portions of a regex pattern that are enclosed in parentheses
# search method returns a tuple of the groups defined by the pattern
def rearrange_name(name):
  # every string that matches the pattern will be stored in the match object with a tuple with two items (as there are two groups)
  result = re.search(r"^(\w*), (\w*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)

# Numeric repetition qualifiers let us specify how many matches we want a pattern to have
# Find every word with five letters within a string
# \b\b matches word limits at the beginning and end of the pattern to indicate we want full words
# {5} specifies five characters, findall returns all pattern matches
print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")) # Prints ['scary', 'ghost']

#  returns all words that are at least 7 characters.
def long_words(text):
  # {7,} from 7 to n, {, 20} up to 20 characters length
  pattern = r"\w{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []

# Looks for a number between square brackets followed by ": " and a set of upper case letters
def extract_pid(log_line):
    regex = r"\[(\d+)\]: ([A-Z]{1,})"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)

# We can use re 's module 'split' method to split strings based on regex
# We are using capturing groups (the parentheses wraping the expression) so every match 
# will be included
print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))

# The sub method is used for creating new strings by substituting all or part of them 
# for a different string, similar to the replace string method but using regular 
# expressions for both the matching and the replacing.
# Replacing every email address by [REDACTED]
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email from add@email.com")) # Received an email from [REDACTED]

# We can use regex as the replace argument of sub too
# \2 \1 means we want to return the second match group followed by the first (OMG)
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")) # Ada Lovelace


# We're working with a CSV file, which contains employee information. 
# Each record has a name field, followed by a phone number field, and a role field. 
# The phone number field contains U.S. phone numbers, and needs to be modified to 
# the international format, with "+1-" in front of the phone number.
def transform_record(record):
  new_record = re.sub(r"([\d]+[-\d]+[-\d]?)", r"+1-\1", record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer


# The multi_vowel_words function returns all words with 3 or more consecutive 
# vowels (a, e, i, o, u).
def multi_vowel_words(text):
  pattern = r"\b\w+[aeiou]{3,}\w+\b"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []


# The convert_phone_number function checks for a U.S. phone number 
# format: XXX-XXX-XXXX (3 digits followed by a dash, 3 more digits 
# followed by a dash, and 4 digits), and converts it to a more formal 
# format that looks like this: (XXX) XXX-XXXX.
def convert_phone_number(phone):
  result = re.sub(r"\b(\d{3})-(\d{3})-(\d{4})\b", r"(\1) \2-\3", phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300