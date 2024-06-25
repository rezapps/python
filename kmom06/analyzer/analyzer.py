# pylint: disable=missing-function-docstring, missing-module-docstring
"""
Du skall skapa funktioner för textanalysering i modulen analyzer.py.

Analysera antal rader (ej tomma), ord och bokstäver med menyvalen lines, 
words och letters. Skriv en funktion för varje kommando.
"""
fileList = ['phil.txt']
changed = 0


def lines():
    linecount = 0
    f = openFile('read')
    rfile = f.readlines()
    for line in rfile:
        if line != '\n':
            linecount += 1
    print(linecount)

def words():
    wordcount = wordCounter()
    print(wordcount)

def letters():
    lettercount = lettercounter('count')
    print(lettercount)
    # return lettercount

def word_freq():
    tot = wordCounter()
    mfv = {}
    f = openFile('read')
    f = f.read()
    freq = f.split()

    for ordet in freq:
        ordet = ordet.lower()
        ordet = ordet.replace(',', '')
        ordet = ordet.replace('.', '')
        ordet = ordet.replace('-', '')
        ordet = ordet.replace('\n', '')
        mfv[ordet] = mfv.get(ordet, 0) + 1
    
    mo_fr_wd = sorted(mfv.items(), key=lambda x: x[1], reverse=True)
    result = frqfunc(mo_fr_wd, tot)
    print(result)
    # return result


def letter_freq():
    ltrList = lettercounter('letterList')
    mfl = {}
    for char in ltrList:
        mfl[char] = mfl.get(char, 0) + 1
    
    mo_fr_ltr = sorted(mfl.items(), key=lambda x: x[1], reverse=True)
    tot = lettercounter('count')
    result = frqfunc(mo_fr_ltr, tot)
    
    print(result)
    # return result

def allfunc():
    lines()
    words()
    letters()
    word_freq()
    letter_freq()
    


def change(fileName):
    openFile('change', fileName)
    # print(fileName)
def quitfunc():
    print("program closed")
def funcNotValid():
    print("That is not a valid choice. You can only choose from the menu.")




def lettercounter(arg):
    result = None
    lettercount = 0
    newList = []
    f = openFile('read')
    f = f.read()
    charslist = f.split()
    for x in charslist:
        for y in x:
            if y not in ['\n', ' ', '-', ',', '.']:
                lettercount += 1
                newList.append(y.lower())
    if arg == 'count':
        result = lettercount
    elif arg == 'letterList':
        result = newList
    return result

def wordCounter():
    wordcount = 0
    fr = openFile('read')
    fr = fr.read()
    wordcount = len(fr.split(' '))
    return wordcount

def frqfunc(arg, tot):
    result = {}
    i = 0
    while i < 7:
        stats = str(arg[i][1]) + ' | ' + '{:.1%}'.format((arg[i][1] / tot))
        result[arg[i][0]] = stats
        i += 1
    return result


def openFile(arg, fileName=''):
    result = None
    
    if arg == 'read':
        with open(fileList[0], 'r'):
            f = open(fileList[0], 'r')
            result = f
    elif arg == 'change' and fileName != '':
        fileList.insert(0, fileName)
    return result
