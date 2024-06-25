# pylint: disable=missing-function-docstring, invalid-name
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This is Main page of Marvin."""


import marvin

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


def main():
    while True:
        # print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Dameon. How can I help you?")
        print("1) Present yourself to Dameon.")
        print("2) Convert Celcius till Farenheit.")
        print("3) Repeat a word multiple times.")
        print("4) Give me a few numbers to calculate the average and sum of those.")
        print("5) Give me a new number to compare it to the last one.")
        print("6) Give me a word to make it funny")
        print("7) Give me a word to check if it is isogram")
        print("8) Give me a word to return a new word made from it")
        print("9) Give me two words to check for anagram: ")
        print("10) Give me a string with a few characters in uppercase to make an acronym: ")
        print("11) Give me a list of numbers to filter those over 10: ")
        print("A1) Give me two strings to check if they match")
        print("A4) Give me two names to make a couple name like 'Brangelina'")
        print("q) Quit.")
        print("Testa den nya inv kommandot: ")

        choice = input("--> ")

        if choice == "1":
            marvin.func1()
        elif choice == "2":
            marvin.func2()
        elif choice == "3":
            marvin.func3()
        elif choice == "4":
            marvin.func4()
        elif choice == "5":
            marvin.func5()
        elif choice == "6":
            marvin.func6()
        elif choice == "7":
            marvin.func7()
        elif choice == "8":
            marvin.func8()
        elif choice == "9":
            marvin.func9()
        elif choice == "10":
            marvin.func10()
        elif choice == "11":
            marvin.func11()
        elif choice == "A1":
            marvin.funcA1()
        elif choice == "A4":
            marvin.funcA4()
        elif len(choice) > 3 and choice[0:3] == 'inv':
            marvin.funcInvs(choice)
        elif choice == 'inv':
            marvin.funcInv()
        elif choice == "q":
            marvin.funcQuit()
            break
        else:
            marvin.funcNotValid()


if __name__ == "__main__":
    print("name: " + __name__)
    main()
