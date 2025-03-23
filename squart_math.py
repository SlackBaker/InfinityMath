import math
import matplotlib.pyplot as plt
import numpy as np  # Додаємо імпорт для numpy

def sqrt(x):
    return math.sqrt(x)

def pow(x, n):
    return x**n

def solve_quadratic(a, b, c):
    D = (b ** 2) - (4 * a * c)
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("x1 = ", x1, " x2 = ", x2)
    else:
        print("error")

def viet_quadratic(x1, x2):
    p = -1 * (x1 + x2)
    q = x1 * x2
    return p, q

def plot_function(func, x_range):
    # Створюємо масив значень x
    x = np.linspace(x_range[0], x_range[1], 1000)

    # Обчислюємо відповідні значення функції
    y = func(x)

    # Створюємо графік
    plt.plot(x, y)

    plt.title("Графік функції")
    plt.xlabel("x")
    plt.ylabel("y")

    # Показуємо графік
    plt.grid(True)
    plt.show()

# example of usage:
def my_function(x):
    return x * np.sqrt(np.abs(x)) * np.sin(x)  # Використовуємо np для стабільності


# draw function from -10 to 10
plot_function(my_function, (-10, 10))

def plot_multiple_functions(functions, x_range):
    x = np.linspace(x_range[0], x_range[1], 1000)
    plt.figure()

    for func in functions:
        y = func(x)
        plt.plot(x, y)

    plt.title("Графіки кількох функцій")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend([f"f{x}" for x in range(1, len(functions)+1)])
    plt.show()

# Використання:
plot_multiple_functions([my_function, lambda x: np.cos(x)], (-10, 10))
