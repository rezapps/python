# pylint: disable=missing-function-docstring, missing-module-docstring


import menu
import analyzer


def main():
    choice = menu.menu()
    if choice == "lines":
        analyzer.lines()
    elif choice == "words":
        analyzer.words()
    elif choice == "letters":
        analyzer.letters()
    elif choice == "word_frequency":
        analyzer.word_freq()
    elif choice == "letter_frequency":
        analyzer.letter_freq()
    elif choice == "all":
        analyzer.allfunc()
    elif choice.split(' ')[0] == "change":
        fileName = choice.split(' ')[1]
        analyzer.change(fileName)
    elif choice == "q":
        analyzer.quitfunc()
        exit()
    else:
        analyzer.funcNotValid()

if __name__ == "__main__":
    while(True):
        main()
