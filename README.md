# Infinitive math
nfinityMath is a Python module designed for advanced mathematical computations. It includes functions for algebra, trigonometry, calculus, quadratic equations, and graphical plotting. This module aims to provide efficient and easy-to-use mathematical tools for students, engineers, and researchers.
# How to use:
# InfinityMath

InfinityMath is a Python module that provides a collection of mathematical functions, including basic arithmetic operations, trigonometric functions, factorial calculation, logarithms, quadratic equation solving, and function plotting.

## Installation

To use this module, simply copy the `InfinityMath` directory into your Python project.
```python
import InfinityMath.algebra
from InfinityMath import algebra
from InfinityMath import trigonometry
from InfinityMath import calculus
from InfinityMath import graphics
from InfinityMath import quadratics_math
```

## Usage

Import the module and use its functions as shown in the examples below:

```python
import InfinityMath.algebra
from InfinityMath import algebra
from InfinityMath import trigonometry
from InfinityMath import calculus
from InfinityMath import graphics
from InfinityMath import quadratics_math

print(InfinityMath.__version__)
#get version

print(InfinityMath.algebra.div(2,5))
print(InfinityMath.algebra.pow(3,5))
# You can use sqrt, sum, substarction and other functions below
roots = InfinityMath.quadratics_math.solve_quadratic(1, -3, 2)
print(roots)  # Outputs the roots of x² - 3x + 2 = 0

from InfinityMath import graphics
import math

def f(x):
    return math.sin(x)

InfinityMath.graphics.plot_function(f, -math.pi, math.pi)

from InfinityMath import calculus
result, error = calculus.integrate_function(lambda x: x**2, 0, 1)
print(result, error)


print(InfinityMath.e)
print(InfinityMath.pi)
```

## Features

- Basic arithmetic operations: `sum`, `subtraction`, `product`, `div`
- Exponential and logarithm functions: `pow`, `log`
- Trigonometric functions: `sin`, `cos`, `tan`, `asin`, `acos`, `atan`
- Factorial calculation: `factorial`
- Quadratic equation solving: `solve_quadratic`, `viet_quadratic`
- Function plotting: `plot_function`, `plot_multiple_functions`

## License

This project is open-source. You are free to modify and distribute it.

