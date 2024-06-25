#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

marvin_image = r"""
             ,       ,
            /(       )`
            \ \__   / |
            /- _ `-/  '
           (/\/ \ \   /\
           / /   | `    \
           O O   )      |
           `-^--'`<     '
          (_.)  _ )    /
           `.___/`    /
             `-----' /
<----.     __ / __   \
<----|====O)))==) \) /=============
<----'    `--' `.__,' \
             |         |
              \       /
          ____( (_   / \______
        ,'  ,----'   |        \
        `--{__________)       \/
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""



while True:
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(marvin_image)
    print("Hi, I'm Dameon. How can I help you?")
    print("1) Present yourself to Dameon.")
    print("2) Convert Celcius till Farenheit.")
    print("3) Repeat a word multiple times.")
    print("4) Give me a few numbers to calculate the average and sum of those.")
    print("5) Give me a new number to compare it to the last one.")
    print("6) Give me a word to make it funny")
    print("7) Give me a word to check if it is isogram")
    print("A1) Give me two strings to check if they match")
    print("A4) Give me two names to make a couple name like 'Brangelina'")
    print("q) Quit.")

    choice = input("--> ")


    if choice == "1":
        name = input("What is your name? ")
        print("\nMarvin says:\n")
        print("Hello %s - your awesomeness!" % name)
        print("What can I do you for?!")

    elif choice == "2":
        tempC = int(input("Give me Temperature in Celcius: "))
        print('It is '+str(tempC * 9/5 +32)+' in Fahrenheit')

    elif choice == "3":
        word = input("Give me a word: ")
        multip = input("\nHow many times should I repeat the word:\n")
        print(word*int(multip))


    elif choice == "4":
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

    elif choice == "5":
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

    elif choice == "6":
        newWord = input('Give me a word to make it fun word: ')
        funword = ''
        x = 1
        while x <= len(newWord):
            funword += str(newWord[x -1] * x) + '-'
            x += 1
        print('input: '+newWord)
        print('output: '+funword)

    elif choice == '7':
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

    elif choice == 'A1':
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

    elif choice == 'A4':
        ord1 = input('Give me first name: ')
        ord2 = input('Give me second name: ')
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        endIndex = 0
        for x in ord1:
            if x in vowels:
                endIndex = ord1.index(x)
                break

        ordMix = ord1[0:endIndex]
        if len(ordMix) == 1:
            print(ordMix + ord2[1:])
        else:
            print(ordMix + ord2)


    elif choice == "q":
        print("Bye, bye - and welcome back anytime!")
        break

    else:
        print("That is not a valid choice. You can only choose from the menu.")

    input("\nPress enter to continue...")
