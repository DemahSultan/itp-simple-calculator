def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    if y !=0: 
        return x / y


def multiply(x, y):
    return x * y


def square(x):
    return x**2


def power(x, y):
    return x**y


def sqrt(x):
    return x**x 


# For the add() function
$ py.test test_add.py

# For the subtract() function
$ py.test test_subtract.py

# For the mulitply() function
$ py.test test_multiply.py

$ py.test test_divide.py
$ py.test test_square.py
$ py.test test_power.py
$ py.test test_sqrt.py
