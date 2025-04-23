# str = "python"
# print(str[-4])
# print(str[-3])
# print(str[-2])
# print(str[-1])
# print(str[-5]) 
# print(str[-6])


# s = "Hello World"
# print(s[1])
# print(s[-1])
# print(s[1:3])
# print(s[1:-1])
# print(s[:3])
# print(s[2:])
# print(s[:-1])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])


# SRING CONCATENATION


# first_name = "Sanjay"
# last_name = "Arjun"
# full_name = first_name +" " + last_name
# print(full_name)

# String Length

# string1 = "Coding is Fun"
# string2 = "Hello,World!"
# string3 = "abcdefghijk"
# string4 = "The quick brown fox jumps over the lazy dog."
# print(len(string1), len(string2), len(string3), len(string4))

# STRING METHODS

# Here's the updated code with all the string methods combined:

# ```python
# Provided code
# ***********************************************************************************************************

# s = "sanju"

# s2 = s.upper()        # Converts to uppercase: 'SANJU'
# s3 = s.lower()        # Converts to lowercase: 'sanju'
# s4 = s.strip()        # Removes whitespace from both ends: 'sanju'
# s5 = s.replace('a', 'u')  # Replaces 'a' with 'u': 'sunju'
# s6 = s.count('s')     # Counts occurrences of 's': 1
# s7 = s.capitalize()   # Capitalizes first letter: 'Sanju'
# s8 = s.title()        # Capitalizes first letter of each word: 'Sanju'
# s9 = s.lstrip()       # Removes whitespace from the left end: 'sanju'
# s10 = s.rstrip()      # Removes whitespace from the right end: 'sanju'
# s11 = s.startswith('s')  # Checks if it starts with 's': True
# s12 = s.endswith('u')    # Checks if it ends with 'u': True

# # String Methods from images
# split_example = s.split('a')            # Splits 'sanju' into ['s', 'nju']
# join_example = '-'.join(['sa', 'nju'])  # Joins into 'sa-nju'

# find_example = s.find('n')      # Finds first occurrence of 'n': 2
# rfind_example = s.rfind('n')    # Finds last occurrence of 'n': 2
# index_example = s.index('n')    # Finds index of first occurrence of 'n': 2
# rindex_example = s.rindex('n')  # Finds index of last occurrence of 'n': 2

# isalnum_example = s.isalnum()   # Checks if alphanumeric: True
# isalpha_example = s.isalpha()   # Checks if alphabetic: True

# # Additional String Methods
# isdigit_example = s.isdigit()       # Checks if all are digits: False
# islower_example = s.islower()       # Checks if all are lowercase: True
# isupper_example = s.isupper()       # Checks if all are uppercase: False
# isspace_example = s.isspace()       # Checks if all are whitespace: False
# isnumeric_example = s.isnumeric()   # Checks if all are numeric: False
# isdecimal_example = s.isdecimal()   # Checks if decimal numbers: False

# startswith_example = s.startswith('s', 0, 3)  # Starts with 's': True
# endswith_example = s.endswith('u', 0, 5)      # Ends with 'u': True

# print(s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12)
# print(split_example, join_example, find_example, rfind_example, index_example, rindex_example, isalnum_example, isalpha_example)
# print(isdigit_example, islower_example, isupper_example, isspace_example, isnumeric_example, isdecimal_example, startswith_example, endswith_example)


# ********************************************************************************************************************************************************************


# STRING FORMATTING
# f string formatting

# name = "sanju"
# age = 20
# print(f"his name is {name} and his age is {age}")



