# pylint: disable=missing-function-docstring, missing-module-docstring
"""
Modulen menu.py skall enbart innehålla kod för att visa menyn.
"""

def menu():
    print('lines) count lines')
    print('words) count words')
    print('letters) count letters')
    print('word_frequency) Find 7 most used words')
    print('letter_frequency) Find 7 most used letters')
    print('all) Do everything')
    print('change) change file "change <fileName>" ie: change fil.txt')
    print('q) quit.')
    choice = input("-->")
    return (choice)
