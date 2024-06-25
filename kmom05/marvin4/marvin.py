# pylint: disable=missing-function-docstring, inconsistent-return-statements, invalid-name, line-too-long
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

import random


marvinsBag = []
def func1():
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")

def func2():
    tempC = int(input("Give me Temperature in Celcius: "))
    print('It is '+str(tempC * 9/5 + 32)+' in Fahrenheit')

def func3():
    word = input("Give me a word: ")
    multip = input("\nHow many times should I repeat the word:\n")
    print(word*int(multip))

def func4():
    numbers = []
    while True:
        print('type "calc" to calculate when you are done!')
        newNum = input("Give me a new number: ")
        if newNum.isdigit():
            numbers.append(int(float(newNum)))
        elif newNum.isdigit() is False and newNum != 'calc':
            newNum = input("That was not a number. Give me a new number: ")
            numbers.append(int(float(newNum)))
        elif newNum == 'calc' and len(numbers) >= 2:
            print('Sum: ' + str(sum(numbers)))
            print('Average: ' + str(sum(numbers) / len(numbers)))
            break

def func5():
    numArr = []
    print('type "done" to end the game!')
    newNum = input("Give me a number: ")
    while True:
        if newNum.isdigit():
            numArr.append(int(float(newNum)))
        if newNum.isdigit() and len(numArr) >= 1:
            newNum = input('Give another number to compare with:')
            if newNum.isdigit():
                numArr.append(int(float(newNum)))
                if numArr[-1] > numArr[-2]:
                    print('The last number ' + str(numArr[-1]) + ' was bigger than ' + str(numArr[-2]))
                elif numArr[-1] < numArr[-2]:
                    print('The last number ' + str(numArr[-1]) + ' was smaller than ' + str(numArr[-2]))
                else:
                    print('They are the same!')
        elif newNum.isdigit() is False and newNum != 'done':
            newNum = input('That was not a number. Give another number to compare with:')
            numArr.append(int(float(newNum)))
        elif newNum == 'done':
            print('Thanks for playing, Bye!')
            break

def func6():
    newWord = input('Give me a word to make it fun word: ')
    funWord = ''
    x = 1
    while x <= len(newWord):
        funWord += str(newWord[x - 1] * x) + '-'
        x += 1
    print('input: '+newWord)
    print('output: '+funWord)

def func7():
    isoWord = input('Give me a word to check for isogram: ')
    x = 0
    word = list(isoWord.lower())
    while len(word) > 0:
        checkWord = word.pop(0)
        if len(word) == 0:
            print('input: ' + isoWord)
            print('output: "Match"')
        elif len(word) >= 1 and checkWord not in word:
            x += 1
        elif checkWord in word:
            print('input: ' + isoWord)
            print('output: "No match"')
            break


def func8():
    nyWord = input('Give me a word: ')
    newWord = list(nyWord)
    random.shuffle(newWord)
    newWord = ''.join(newWord)
    print(newWord)

def func9():
    word1 = input('Give me the first word: ').lower()
    word2 = input('Give me the second word: ').lower()
    wordList1 = list(word1)
    wordList2 = list(word2)
    result = ''
    for x in wordList1:
        if x not in wordList2:
            result = 'No Match'
        else:
            result = 'Match'

    # wordList1.sort()
    # wordList2.sort()
    # if wordList1 == wordList2:
    #     result = 'Match'
    # else:
    #     result = 'No MaTCH'

    print(result)


def func10():
    str1 = input('Give me a string with a few words in uppercase to make an acronym: ')
    str1List = list(str1)
    acronymWord = []
    for x in str1List:
        if x.isupper():
            acronymWord.append(x)
    print(''.join(acronymWord))


def func11():
    userNum = input('Give me a list of numbers separated by space: ')
    numList = userNum.split(" ")

    for x in numList:
        y = int(x)
        l = numList.index(x)
        numList.remove(x)
        numList.insert(l, y)
    filteredList = filter(None, numList)

    def filter_nums(x):
        if x > 10:
            return x
    filtered_Num = filter(filter_nums, filteredList)
    print(list(filtered_Num))
    return list(filtered_Num)




def funcA1():
    matchword = input('Give me the first word: ')
    word2 = input('Give me the second word: ')
    x = 0
    while x < len(word2):
        if word2[x] not in matchword:
            print('input: ' + matchword + ', ' + word2)
            print('output: No match')
            x = len(word2)
        elif x == len(word2) - 1:
            print('input: ' + matchword + ', ' + word2)
            print('output: Match')
            x = len(word2)
        else:
            x += 1

def funcA4():
    ord1 = input('Give me first name: ')
    ord2 = input('Give me second name: ')
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    endIndex = 0
    for x in ord1:
        if x in vowels:
            endIndex = ord1.index(x)
            break

    ordMix = ord1[0:endIndex]
    mixedOrd = ''
    if len(ordMix) == 1:
        mixedOrd = ordMix + ord2[1:]
    else:
        mixedOrd = ordMix + ord2
    print(mixedOrd)



# elif len(choice) > 3 and choice[0:3] == 'inv':
def funcInvs(choice):
    inv = choice.split(' ')
    targetItem = inv[2]

    if len(inv) <= 3 and inv[1] == 'pick':
        marvinsBag.append(targetItem)
        print(targetItem + ' has been added.')

    elif len(inv) > 3 and inv[1] == 'pick':
        newIndex = int(inv[3])
        if newIndex < len(inv):
            marvinsBag.insert(newIndex, targetItem)
            print(str(targetItem) + ' has been added to index: ' + str(newIndex))
        else:
            print('There is no pocket number ' + newIndex + ' in my bag. But I put it in the last one')
            marvinsBag.append(targetItem)
        print(marvinsBag)

    elif inv[1] == 'drop':
        if targetItem in marvinsBag:
            marvinsBag.remove(targetItem)
            print(marvinsBag)
            print(targetItem + ' has been deleted.')
        else:
            print('I do not have ' + targetItem+' in my bag!')

    elif inv[1] == 'swap':
        item1 = inv[2]
        item1Indx = marvinsBag.index(item1)
        print(item1Indx)
        item2 = inv[3]
        item2Indx = marvinsBag.index(item2)
        print(item2Indx)

        if item2Indx > item1Indx:
            del marvinsBag[item1Indx]
            print(marvinsBag)
            marvinsBag.insert(item1Indx, item2)
            print(marvinsBag)
            del marvinsBag[item2Indx]
            print(marvinsBag)
            marvinsBag.insert(item2Indx, item1)
        else:
            del marvinsBag[item2Indx]
            marvinsBag.insert(item2Indx, item1)
            del marvinsBag[item1Indx]
            marvinsBag.insert(item1Indx, item2)
            print(marvinsBag)

        print(marvinsBag)
        print(item1 + ' swaped with ' + item2)


def funcInv():
    if len(marvinsBag) > 0:
        print('Backpack has ' + str(len(marvinsBag)) + \
                ' items: ' + str(marvinsBag))
    else:
        print('My bag is empty now.')


def funcQuit():
    print("Bye, bye - and welcome back anytime!")


def funcNotValid():
    print("That is not a valid choice. You can only choose from the menu.")

# input("\nPress enter to continue...")
