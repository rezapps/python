#!/usr/bin/env python3
# pylint: disable=missing-docstring


"""
c6d9f1abae45c1c8539354f544d7b8e7
python
lab3
v4
rere20
2020-09-05 14:39:15
v4.0.0 (2019-03-05)

Generated 2020-09-05 16:39:15 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()


# ==========================================================================
# Lab 3 - python
#
# "In these exercises we will take a look into lists."
#


# --------------------------------------------------------------------------
# Section 1. List basics
#
#
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Concatenate the two lists [Whitaker, Dafoe] and [fly, Dafoe].
#
# Answer with your list.
#
# Write your code below and put the answer into the variable ANSWER.
#

list1 = ['Whitaker', 'Dafoe']
list2 = ['fly', 'Dafoe']

for x in list2:
    list1.append(x)


ANSWER = list1

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Use the list [wasp, fly, butterfly, bumblebee, mosquito].
#
# Add the words 'purple' and 'bag' as the second and third element.
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

list3 = ['wasp', 'fly', 'butterfly', 'bumblebee', 'mosquito']
newList = ['purple', 'bag']

y = 1

for x in newList:
    list3.insert(y, x)
    y += 1


ANSWER = list3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Use the list [wasp, fly, butterfly, bumblebee, mosquito].
#
# Replace the third word with: 'light'.
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

list4 = ['wasp', 'fly', 'butterfly', 'bumblebee', 'mosquito']
word3 = 'light'

list4.pop(2)
list4.insert(2, word3)


ANSWER = list4

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Sort the list
#
# > [Dafoe, Sheen, Berenger, Depp, Whitaker]
#
# in descending alphabetical order. Answer with the sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#

list5 = ['Dafoe', 'Sheen', 'Berenger', 'Depp', 'Whitaker']

list5.sort(reverse=True)


ANSWER = list5

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Use `remove()` to delete the word:
#
# > 'butterfly'
#
# from the list:
#
# > [wasp, fly, butterfly, bumblebee, mosquito]
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

list6 = ['wasp', 'fly', 'butterfly', 'bumblebee', 'mosquito']

list6.remove('butterfly')


ANSWER = list6

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Built-in list functions
#
# Some basic built-in functions.
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Use a built-in function to sum all numbers in the list:
#
# > [45, 22, 2, 498, 78]
#
# Answer with the result as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#

list7 = [45, 22, 2, 498, 78]
totList7 = sum(list7)


ANSWER = totList7

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Use built-in functions, such as `sum` and `len` to get the average value of
# the list:
#
# > [567, 23, 12, 36, 7]
#
# Answer with the result as a float with at most one decimal.
#
# Write your code below and put the answer into the variable ANSWER.
#

list8 = [567, 23, 12, 36, 7]
lenList8 = len(list8)

sumList8 = sum(list8)

aveList8 = sumList8 / lenList8

ANSWER = aveList8

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Use the built-in functions `split()` and `join()` to fix this string:
#
# > "The?snow?is?falling"
#
# into a real sentence, (without '?').
#
# Answer with the fixed string.
#
# Write your code below and put the answer into the variable ANSWER.
#

str1 = "The?snow?is?falling"
str1 = str1.split('?')

str1 = ' '.join(str1)


ANSWER = str1

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Use slice on the list
#
# > [tree, stone, grass, water, sky]
#
# and replace the second and third element with
#
# > "book, candle"
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

list9 = ['tree', 'stone', 'grass', 'water', 'sky']

list9[1:3] = ['book', 'candle']


ANSWER = list9

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.5 (1 points)
#
# Assign the list
#
# > [a, b, c, d, e]
#
# to a variable called 'list1'.
#
# Assign the list again, but to another variable called 'list2'.
#
# Answer with the result of 'list1 is list2'.
#
# Write your code below and put the answer into the variable ANSWER.
#

list10 = ['a', 'b', 'c', 'd', 'e']
list11 = ['p', 'b', 'c', 'd', 'e']

listCompare = list10 is list11


ANSWER = listCompare

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.6 (1 points)
#
# Use your lists from the last exercise. Assign 'list1' to another variable
# called 'list3' like this:
#
# > list3 = list1
#
# Answer with the result of 'list1 is list3'.
#
# Write your code below and put the answer into the variable ANSWER.
#

list12 = list11

listCompare2 = list12 is list11


ANSWER = listCompare2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.7 (1 points)
#
# Use your lists from the last exercise. Change the first element in 'list1'
# to
#
# > "p"
#
# Answer with 'list3'.
#
# Write your code below and put the answer into the variable ANSWER.
#


ANSWER = list12

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.7", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Create a function that returns the list passed as argument sorted in
# numerical and ascending order. Also multiply all values with 10.
#
# Use the list:
#
# > [567, 23, 12, 36, 7]
#
# and the built-in method `sort()`.
#
# Answer with the sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#

list14 = [567, 23, 12, 36, 7]


def sortMultiply(aList):
    m = 0
    while m < len(aList):
        n = aList[m] * 10
        aList.pop(m)
        aList.insert(m, n)
        m += 1
    aList.sort()
    return aList


sortedList1 = sortMultiply(list14)


ANSWER = sortedList1

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Create a function that takes the list:
#
# > [567, 23, 12, 36, 7]
#
# as argument.
#
# The function should multiply all even numbers by 1 and add 5 to all odd
# numbers.
#
# Answer with the modified list sorted in numerical order, descending.
#
# Write your code below and put the answer into the variable ANSWER.
#


list15 = [567, 23, 12, 36, 7]


def makeEven(aList):
    z = 0
    while z < len(aList):
        if aList[z] % 2 > 0:
            i = aList[z] + 5
            aList.pop(z)
            aList.insert(z, i)
        z += 1
    aList.sort(reverse=True)
    return aList


sortedList2 = makeEven(list15)


ANSWER = sortedList2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
