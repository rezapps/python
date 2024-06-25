# functions.py
# pylint: disable=missing-docstring
def greater():
    return "Hi, the weather is nice today!"


def funny_word(word):
    return word + ' is a funny word'


def double_decider(word1, word2):
    modedWord1 = decider(word1)
    modedWord2 = decider(word2)
    return modedWord1 + modedWord2


def decider(word):
    x = ''
    if isinstance(word, int):
        y = word * word
        x = ' and the square is ' + str(y)
    else:
        x = funny_word(word)
    return x
