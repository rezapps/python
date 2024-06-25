#!/usr/bin/env python3

"""
0cc0ee99ef5b2366e89faedc45130c1e
python
lab5
v4
rere20
2020-09-30 19:48:23
v4.0.0 (2019-03-05)

Generated 2020-09-30 21:48:23 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 5 - python
#
# A look into dictionaries and tuples.
#



# --------------------------------------------------------------------------
# Section 1. Dictionaries
#
# Some basics with dictionaries.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a small phonebook using a dictionary. Use the names as keys and
# numbers as values.
#
# Use
#
# > Solo, Skywalker, Vader
#
# and corresponding numbers
#
# > 55511243, 55568711, 55590858
#
# Add the phonenumbers as integers. Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#

answer1_1 = {'Skywalker':55568711, 'Solo':55511243, 'Vader':55590858}




ANSWER = answer1_1

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# How many items are there in the phonebook dictionary?
#
# Write your code below and put the answer into the variable ANSWER.
#

answer1_2 = len(answer1_1.items())




ANSWER = answer1_2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Use the `get()` method on your phonebook and answer with the phonenumber of
# 'Skywalker'.
#
# Write your code below and put the answer into the variable ANSWER.
#


answer1_3 = answer1_1.get('Skywalker')



ANSWER = answer1_3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Get all keys from the phonebook dictionary and return them in a sorted
# list.
#
# Write your code below and put the answer into the variable ANSWER.
#


answer1_4 = []
for k, v in answer1_1.items():
    answer1_4.append(k)



ANSWER = answer1_4

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Get all values from the phonebook dictionary and return them in a sorted
# list.
#
# Write your code below and put the answer into the variable ANSWER.
#


answer1_5 = []
for k, v in answer1_1.items():
    answer1_5.append(v)



ANSWER = sorted(answer1_5)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Use the in-operator to test if the name 'Skywalker' exists in the phonebook
# dictionary. Answer with the return boolean value.
#
# Write your code below and put the answer into the variable ANSWER.
#


answer1_6 = 'Skywalker' in answer1_1



ANSWER = answer1_6

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# Create a copy of the phonebook dictionary.
# Get and remove the item 'Skywalker' from the copied phonebook (use pop()).
# Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Tuples
#
# Some basics with tuples.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Create a tuple with 'moose, 12, 1.98, table, 7'. Answer with the length of
# the tuple as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Create a tuple out of:
#
# > (moose, 12, 1.98, table, 7).
#
# Assign each value in the tuple to different variables:
#
# > 'a','b','c','d','e'.
#
# Answer with the variable: 'd'.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Use the list
#
# > [45, 22, 2, 498, 78]
#
# Assign the first two elements to a tuple with a slice on the list.
#
# Answer with the first element in the tuple as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Create a tuple with
#
# > (bear, 65, 6.47, chair, 5)
#
# Convert it to a list and replace the second element with:
#
# > "green"
#
# Convert it back to a tuple and answer with the first three elements in a
# comma-separated string,  without an ending `,`.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Use a for-loop to walk through the original phonebook dictionary and create
# a string representing it. Each name and number should be on its own row,
# separated by a space. The names must come in alphabetical order. Note that
# every row should end with a newline character, `\n`.
#
# Answer with the resulting string.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Convert the phonenumber to a string and add the prefix '+1-', representing
# the language code, to each phone-number.
#
# Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
