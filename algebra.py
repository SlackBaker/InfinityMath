import math

def pow(x, n):
    return x**n

def sum(x1, x2):
    return x1 + x2

def subtraction(x1, x2):
    return x1 - x2

def product(x1, x2):
    return x1 * x2

def div(x1, x2):
    if x2 == 0:
        raise ValueError("Division by zero is not allowed")
    return x1 / x2

def factorial(x):
    return math.factorial(x)

def log(x, base=10):
    return math.log(x, base)

def sqrt(x):
    return math.sqrt(x)