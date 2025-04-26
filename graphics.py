import matplotlib.pyplot as plt
import numpy as np

def plot_function(func, x_range, label="f(x)", color="b"):
    x = np.linspace(x_range[0], x_range[1], 1000)
    y = func(x)
    plt.plot(x, y, color, label=label)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_multiple_functions(functions, x_range, labels=None, colors=None):
    x = np.linspace(x_range[0], x_range[1], 1000)
    plt.figure()
    if labels is None:
        labels = [f"f{x}" for x in range(1, len(functions) + 1)]
    if colors is None:
        colors = ["b", "g", "r", "c", "m", "y", "k"] * 2  # Повторюваний список кольорів
    for func, label, color in zip(functions, labels, colors):
        y = func(x)
        plt.plot(x, y, color, label=label)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.show()