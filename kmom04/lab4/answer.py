#!/usr/bin/env python3
# pylint: disable=missing-docstring

"""
723f6c5818af6f7ca01a614c367932cf
python
lab4
v4
rere20
2020-09-06 18:51:43
v4.0.0 (2019-03-05)

Generated 2020-09-06 20:51:43 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb
from functions import greater, double_decider, funny_word


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()


# ==========================================================================
# Lab 4 - python
#
# In this lab we take another look at functions and we use modules to
# structure our code.
#


# --------------------------------------------------------------------------
# Section 1. Functions
#
#
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a function `valid_password` that takes one string argument. Check
# whether the argument is a valid password according to the following rules:
#
# * 8 characters or longer
# * Contains upper and lowercase letters
# * Contains a number
#
# The function should return True or False depending on whether the password
# is valid.
#
# Answer with the return value of the function when called with the string
# 'Se3ret'.
#
# Tip: Use built-in character functions `isupper()`, `islower()`,
# `isdigit()`.
#
# Write your code below and put the answer into the variable ANSWER.
#


def valid_password(word):
    hasUpp = False
    hasInt = False
    hasLow = False
    passLen = len(word)
    x = False
    if passLen < 8:
        x = False
    else:
        for x in word:
            if x.isupper():
                hasUpp = True
            elif x.islower():
                hasLow = True
            elif x.isdigit():
                hasInt = True

    if hasUpp and hasInt and hasLow:
        x = True
    elif hasUpp is False or hasInt is False or hasLow is False:
        x = False
    else:
        x = False
    return x


answerOne = valid_password('Se3ret')

ANSWER = answerOne

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Using the function `valid_password` answer with the return value of the
# function when called with the string 'mYsecretpassw0rd'.
#
# Write your code below and put the answer into the variable ANSWER.
#
answerTwo = valid_password('mYsecretpassw0rd')

ANSWER = answerTwo

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a function `number_of_vowels` that takes one argument. The function
# returns the number of vowels (vokaler) in the given argument. The following
# letters is used as vowels in this exercise: aeiouy
#
# Answer with the number of vowels in the following text:
#
# 'And finally, that the source of our dissatisfaction lies in our impulsive
# dependency on our reflexive senses rather than logic.'
#
# Write your code below and put the answer into the variable ANSWER.
#

testSentence1 = 'And finally, that the source of our dissatisfaction lies in our impulsive \
    dependency on our reflexive senses rather than logic.'


def number_of_vowels(word):
    foundVowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for x in word:
        y = x.lower()
        if y in vowels:
            foundVowels += 1
    return foundVowels


answerThree = number_of_vowels(testSentence1)

ANSWER = answerThree

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a function `analyze_password` that uses `valid_password` and
# `number_of_vowels`. The function should return whether or not a password is
# valid and how many vowels the given password contains concatenated to a
# string.
#
# Example: With the input value Se3ret the function should return the
# following string: 'Se3ret is not a valid password and contains 2 vowels.'.
#
# With the input value mYsecretPASSW0rd the function should return the
# following string: 'mYsecretPASSW0rd is a valid password and contains 4
# vowels.'.
#
# Answer with the return value of the function `analyze_password` called with
# the following argument: mYsecretPASSW0rd.
#
# Write your code below and put the answer into the variable ANSWER.
#


def analyze_password(word):
    vowCount = number_of_vowels(word)
    passValid = valid_password(word)
    x = ''
    if passValid:
        x = word + ' is a valid password and contains ' + str(vowCount) + ' vowels.'
    else:
        x = word + ' is not a valid password and contains ' + str(vowCount) + ' vowels.'
    return x


ANSWER = analyze_password('mYsecretPASSW0rd')

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Modules
#
# In this section we will look into modules and how we can structure our
# code.
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Create a new Python file called `functions.py`. Import your new file/module
# in `answer.py` using the import statement: `import functions`
#
# In your new module, create a function called `greeter` that returns `"Hi,
# the weather is nice today!"`.
#
# Answer with the return value from a call to the function.
#
# Write your code below and put the answer into the variable ANSWER.
#

answer2_1 = greater()

ANSWER = answer2_1

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# In your new module, create a function called `funny_word` that takes one
# argument and prepends it to the string ' is a funny word'. **EXAMPLE:** If
# the argument is 'water', the function should return: `"water is a funny
# word"`.
#
# Use the argument 'sunshine' and answer with a call to the function.
#
# Write your code below and put the answer into the variable ANSWER.
#

answer2_2 = funny_word('sunshine')

ANSWER = answer2_2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# In your new module, create a function called `double_decider`. The function
# takes two arguments. For each argument call the `decider` function.
# Concatenate the returned values in a string.
#
# Separate the two values by ' and the square is '.
#
# Answer with a call to the function `double_decider` with the values:
# crudivore and 49 as arguments.
#
# Write your code below and put the answer into the variable ANSWER.
#

answer2_3 = double_decider('crudivore', 49)

ANSWER = answer2_3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)


dbwebb.exit_with_summary()
