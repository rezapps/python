# pylint: disable=missing-docstring, redefined-outer-name
x = "global variable"

def first_global():
    print("calling x from inside a function:", x)

first_global()
print("calling x outside:", x)



def second_global():
    # x = x * 2 
    # felmeddelande: using variable x before assignment
    print(x)

second_global()



# ###############  local variables  ###############
def first_local():
    y = "local variable"
    print(y)

first_local()
# print(y)
# felmeddelande: y is not defined



def second_local():
    y = "local variable"
    print(y)

second_local() # prints: local variable



y = "global variable"
def third_local():
    y = "local variable"
    print("y local variable:", y) # prints: y local variable: local variable

third_local()
print("y global variable:", y) # prints: y global variable: global variable



def funcfoo():
    global x
    x = x * 2
    print("x from inside a function:", x) # prints: x from inside a function: global 
    # variableglobal variable

funcfoo()
print("x from outside function:", x) # prints: x from outside function: global 
# variableglobal variable


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("calling x from inside inner function:", x)

    inner()
    print("calling x from inside outer function:", x)

outer()
