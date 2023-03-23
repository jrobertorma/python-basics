import re 
  
my_txt = "An investment in knowledge pays the best interest."

def LetterCompiler(txt):
    result = re.findall(r'([a-c]).', txt)
    return result

print(LetterCompiler(my_txt))

import unittest

class TestCompiler(unittest.TestCase):

    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)

class TestCompiler2(unittest.TestCase):
    
    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

# EDGE CASES HERE
    def test_three(self):
        testcase = "Ñoño"
        expected = []
        self.assertEqual(LetterCompiler(testcase), expected)
        
    def test_four(self):
        testcase = "abcdefg"
        expected = ['a', 'b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)
        
    def test_five(self):
        testcase = "123123123123123123"
        expected = []
        self.assertEqual(LetterCompiler(testcase), expected)

# Exceptions and Assertions
my_list = [27, 5, 9, 6, 8]

def RemoveValue(myVal):
    my_list.remove(myVal)
    return my_list

print(RemoveValue(27))

# raising an error
def RemoveValue(myVal):
    if myVal not in my_list:
        raise ValueError("Value must be in the given list")
    else:
        my_list.remove(myVal)
    return my_list

print(RemoveValue(27))

# Asserting data types
my_word_list = ['east', 'after', 'up', 'over', 'inside']

def OrganizeList(myList):
    myList.sort()
    return myList

print(OrganizeList(my_word_list)) # ['after', 'east', 'inside', 'over', 'up']

my_new_list = [6, 3, 8, "12", 42]
print(OrganizeList(my_new_list)) # error

# Handling data type errors
def OrganizeList(myList):
    for item in myList:
        assert type(item) == str, "Word list must be a list of strings"
    myList.sort()
    return myList

print(OrganizeList(my_new_list))

# try/catch structure
def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    try:
        if my_participant_dict['Larry'] == 9:
            return True
        else:
            return False
    except KeyError:
        return None

participants = ['Jack','Jill','Larry','Tom']
print(Guess(participants)) # sometimes False lol

participants = ['Cathy','Fred','Jack','Tom']
print(Guess(participants)) # None