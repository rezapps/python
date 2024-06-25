#!/usr/bin/env python3

"""
3437f64da38cabf0fe1f0e1a4a9da010
python
lab2
v4
rere20
2020-09-02 19:31:52
v4.0.0 (2019-03-05)

Generated 2020-09-02 21:31:52 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()


# ==========================================================================
# Lab 2 - python
#
# In this exercise we will look into flow-control. If-statements, for-loops
# and while-loops.
#


# --------------------------------------------------------------------------
# Section 1. Boolean operators and if-statements
#
# The basics of boolean operators and if-statements.
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create three variables representing dice values: `dice1` = 3, `dice2` = 6
# and `dice3` = 3.
#
# Answer with the boolean value of the expression '`dice1` is greater than
# `dice2`'.
#
# Write your code below and put the answer into the variable ANSWER.
#

dice1 = 3
dice2 = 6
dice3 = 3

jamfor1 = dice1 > dice2


ANSWER = jamfor1

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Sum the three variables `dice1`, `dice2` and `dice3`.
#
# Use an if-statement to decide if the sum of the three variables i greater
# than 11. If the sum is greater than 11 answer with 'big' otherwise answer
# with 'small'.
#
# Write your code below and put the answer into the variable ANSWER.
#

sumDice = dice1 + dice2 + dice3
diceAnswer = ''
if sumDice > 11:
    diceAnswer = 'big'
else:
    diceAnswer = 'small'


ANSWER = diceAnswer

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Add the sum of `dice4` = 4 and `dice5` = 1 to the sum of the three other
# dices.
#
# Use an if, elseif, else statement to check the total value of the dices.
# Answer with 'small' if the sum is smaller than 11, 'intermediate' if the
# sum is greater than or equal to 11 but smaller than 21. If the sum is
# greater than or equal to 21 answer with 'big'.
#
# Write your code below and put the answer into the variable ANSWER.
#

dice4 = 4
dice5 = 1

diceAnswer2 = ''

sumDice += dice4 + dice5

if sumDice < 11:
    diceAnswer2 = 'small'
elif sumDice >= 11:
    diceAnswer2 = 'intermediate'
elif sumDice >= 21:
    diceAnswer2 = 'big'


ANSWER = diceAnswer2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a variable `summer_word` containing the word 'restaurant'.
#
# Answer with True if `summer_word` contains the letter 's' otherwise answer
# with False.
#
# Tip: Use the `in` operator.
#
# Write your code below and put the answer into the variable ANSWER.
#

summer_word = 'restaurant'

hitta = 's' in summer_word


ANSWER = hitta

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. For-loops
#
# The basics of iteration and for-loops.
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Loop through the numbers 0 to 10 (10 included) and concatenate a string
# with the numbers comma-separated. You should have a comma at the end of the
# string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#

nummer = ''
for x in range(11):
    nummer = nummer + str(x) + ','


ANSWER = nummer

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Loop through the letters of the variable `summer_word` from above.
# Concatenate the consonants from `summer_word` and answer with the new word.
#
# Tip: Create a string that contains consonants and check if each letter is
# in it.
#
# Write your code below and put the answer into the variable ANSWER.
#

wordd = ''
vowels = ['a', 'e', 'i', 'o', 'u']
for x in summer_word:
    if x not in vowels:
        wordd = wordd+x

ANSWER = wordd

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Loop through all numbers from 42 to 79 both numbers included. Add all odd
# (udda) numbers together and answer with the result.
#
# Tip: Use the modulus % operator.
#
# Write your code below and put the answer into the variable ANSWER.
#

odds = 0
for x in range(42, 80):
    if (x % 2 > 0):
        odds += x


ANSWER = odds

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. While-loops
#
# The basics of while-loops.
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (1 points)
#
# Create a while-loop that starts at value 6 and ends when the value is
# greater than 29, the value should be incremented by 3 for each iteration.
# Concatenate a string with the values comma-separated. You should have a
# comma at the end of the string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#

wloop = ''
i = 6
while i < 29:
    wloop = wloop + str(i) + ','
    i += 3

ANSWER = wloop

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (1 points)
#
# Create a while-loop that subtracts 5 from 90, 71 times. Answer with the
# result.
#
# Write your code below and put the answer into the variable ANSWER.
#

baseN = 90
i = 0
while i < 71:
    baseN -= 5
    i += 1

ANSWER = baseN

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.3 (1 points)
#
# Create a while-loop that calculates the factorial number for 5, 5!. The
# factorial of a number is the number multiplied by all smaller integers
# greater than 1. The factorial of 5 is `5 * 4 * 3 * 2 * 1`. Answer with the
# result.
#
# Write your code below and put the answer into the variable ANSWER.
#

i = 1
base = 5
facto = 1
while i <= base:
    facto *= i
    i += 1


ANSWER = facto

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.3", ANSWER, False)

# --------------------------------------------------------------------------
# Section 4. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 4.1 (3 points)
#
# Use a for-loop or a while-loop to reverse the word 'constitutionality'.
#
# Answer with the reversed word.
#
# Write your code below and put the answer into the variable ANSWER.
#

baseWord = 'constitutionality'
reversedWord = ''
i = len(baseWord)

while i > 0:
    reversedWord = reversedWord + baseWord[i-1]
    i -= 1


ANSWER = reversedWord

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("4.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 4.2 (3 points)
#
# Swedish numberplates consist of three letters and three numbers. The
# numbers range from 001 to 999. Using one of the four common rules of
# arithmetics (+, -, *, /), on how many of the numberplates can the two first
# numbers give the third number?
#
# Examples:
# 'ABC123' can be combined to 1 + 2 = 3. So this numberplate is good.
# 'ABC129' 1 and 2 cannot be combined to give 9 using the four rules of
# arithmetics, so this does not work.
#
# Order matters, so only use 1 +-*/ 2 = 3 and not 2 +-/* 1 = 3.
#
# Do not count multiple times if more than one rule of arithmetics work.
#
# Answer with the number of numberplates.
#
# Write your code below and put the answer into the variable ANSWER.
#

plates = 0
for x in range(0, 10):
    for y in range(0, 10):
        if x + y < 10:
            plates += 1
            # print('ABC'+str(x)+str(y)+str(x+y))
        elif x * y < 10:
            plates += 1
            # print('ABC'+str(x)+str(y)+str(x*y))
        elif x - y >= 0:
            plates += 1
            # print('ABC'+str(x)+str(y)+str(x-y))
        elif x / y >= 0 and x % y == 0:
            plates += 1
            # print('ABC'+str(x)+str(y)+str(x/y))


ANSWER = plates
# print(plates)
# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("4.2", ANSWER, False)


dbwebb.exit_with_summary()
