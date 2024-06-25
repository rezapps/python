#!/usr/bin/env python3
# pylint: disable=consider-using-in

"""
451773eebebca6eba4dbfa6d4477fd4a
python
lab6
v4
rere20
2020-10-16 19:34:57
v4.0.0 (2019-03-05)

Generated 2020-10-16 21:34:57 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()


# ==========================================================================
# Lab 6 - python
#
# During these exercises we train on reading, writing and appending data to
# text file's.
#


# --------------------------------------------------------------------------
# Section 1. Files
#
#
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Read the `ircLog.txt` -file in UTF-8 encoding and store the content into a
# variable. Answer with the number of characters in the file.
#
# Write your code below and put the answer into the variable ANSWER.
#


f = open('ircLog.txt', encoding="utf-8")

data = f.read()

count = len(data)


ANSWER = count

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Use your variable from the exercise above and answer with the contents on
# line number 84.
#
# Write your code below and put the answer into the variable ANSWER.
#


with open('ircLog.txt') as file:
    for _ in range(83):
        foundLine = file.readline()
    found = file.readline()

ans1_2 = found.rstrip()


ANSWER = ans1_2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# First, read the content inside of ircLog.txt. Remove the two last rows and
# replace line number 9 with the new string "I am replaced".
# Then, create a new file called `newLog.txt` where you save the new changes.
# Replace `newLog.txt` if it already exists.
#
# Answer with the new content inside `newLog.txt`. Don't have a "\n" on the
# last line.
#
# Write your code below and put the answer into the variable ANSWER.
#


newText = ''
with open('ircLog.txt', 'r') as rf:
    with open('newLog.txt', 'r+') as wf:
        rfile = rf.readlines()
        rfile = rfile[:-1]
        rfile = rfile[:-1]
        rfile[8] = 'I am replaced\n'
        lastrad = len(rfile) - 1
        rfile[lastrad].rstrip()

        wf.truncate(0)
        rfile = ''.join(rfile).rstrip()
        wf.write(rfile)


ans1_3_1 = open('newLog.txt', encoding="utf-8")

ans1_3 = ans1_3_1.read()


ANSWER = ans1_3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Append the following sentence to the end of newLog.txt and answer with the
# content.
#
# *"-- End of file --"*
#
# Write your code below and put the answer into the variable ANSWER.
#

# with open('newLog.txt', 'r') as rf:
#     with open('newLog.txt', 'r+') as wf:
#         rfile = rf.readlines()
#         rfile.append("-- End of file --")

#         rfile = ''.join(rfile).rstrip()
#         wf.truncate(0)
#         wf.write(rfile)

with open('newLog.txt', 'r+') as wf:
    rfile = wf.readlines()
    rfile.append("\n-- End of file --\n")

    rfile = ''.join(rfile).rstrip()
    wf.truncate(0)
    wf.write(rfile)

ans1_4_1 = open('newLog.txt')

ans1_4 = ans1_4_1.readlines()
ans1_4 = ''.join(ans1_4)


ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Store the number of empty lines `passwords.txt` has and create a new file
# called `newPasswords.txt` containing the lines that are not empty.
#
# Answer with the following:
#
# *passwords.txt has X empty lines and contains: Y*
#
# Replace `X` with the number of empty lines and `Y` with the new files
# content.
#
# Write your code below and put the answer into the variable ANSWER.
#

count = 0
xfile = []
with open('passwords.txt', 'r') as rf:
    with open('newPasswords.txt', 'r+') as wf:
        rfile = rf.readlines()
        wf.truncate(0)
        for line in rfile:
            if line == '' or line == '\n':
                count = count + 1
            elif line != '' or line != '\n':
                xfile.append(line)
        xfile = ''.join(xfile)
        wf.write(xfile)

passfile = open('newPasswords.txt')
Y = passfile.read()
Y = ''.join(Y)

lineCount = 'passwords.txt has ' + \
    str(count) + ' empty lines and contains: ' + Y


ANSWER = lineCount

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Extra assignment
#
# Solve this question for extra points.
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (3 points)
#
# Write the content of line numbers 84, 85 and 86 from `ircLog.txt` to a new
# file that you create called `extraLog.txt`. Replace `extraLog.txt` if it
# already exists.
# Save the total number of characters and the 9 first characters of the
# second line into variables.
#
# Answer with the following string:
# "The file has X characters and the 9 first of the second row are: Y"
#
# **Example**:
# *"The file has 220 characters and the 9 first of the second row are: 00:00
# abc"*
#
# Do not include newlines when you count the number of characters.
#
# Write your code below and put the answer into the variable ANSWER.
#

count = 0
xfile = []
countstart = 83
with open('ircLog.txt', 'r') as rf:
    with open('extraLog.txt', 'r+') as wf:
        rfile = rf.readlines()
        wf.truncate(0)
        count = len(rfile)
        while countstart < 86:
            xfile.append(rfile[countstart])
            countstart += 1
        xfile = ''.join(xfile)
        wf.write(xfile)

newfile = open('extraLog.txt')
newfileread = newfile.read()

newfileLine = newfileread.replace('\n', '')
charscount = len(newfileLine)

secline = newfileread.split('\n')
first9 = secline[1][:9]

answer = 'The file has ' + \
    str(charscount) + ' characters and the 9 first of the second row are: ' + first9


ANSWER = answer

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)


dbwebb.exit_with_summary()
