import matplotlib.pyplot as plt
from sympy import algebras as alg
from sympy.solvers.solvers import solve
from sympy import symbols as symbol
import sympy as sp
import math
import numpy as np
ax = plt.gca


"""
Welcome to the Mathematical Functions Library!

This Python code provides functions for plotting and solving various mathematical problems, including quadratics, sequences, series, and radicals. Below is a quick guide on how to use each function:

1. **Quadratics**:
   - `vertex_quadratic(a, p, q)`: Plots a quadratic equation in vertex form. You can adjust the values of 'a', 'p' (horizontal shift), and 'q' (vertical shift).
   - `standard_quadratic(a, b, c)`: Plots a quadratic equation in standard form. Provide the values of 'a', 'b', and 'c' as the coefficients of the equation.
   - `factored_quadratic(a, X_1, X_2)`: Plots a quadratic equation in factored form. Use 'a' as the coefficient and 'X_1' and 'X_2' as the roots of the equation.
   - `quadratic_formula(a, b, c)`: Returns the roots (solutions) of the quadratic equation `ax^2 + bx + c = 0` using the quadratic formula.

2. **Sequences and Series**:
   - `geometric_sequence(a, r, n)`: Returns the nth term of a geometric sequence. Enter 'a' for the first term, 'r' for the common ratio, and 'n' for the term number.
   - `geometric_series_fin(a, r, n)`: Calculates the sum of the first 'n' terms in a geometric series. Enter 'a', 'r', and 'n'.
   - `geometric_series_infin(a, r)`: Calculates the sum of an infinite geometric series, only if the absolute value of 'r' is less than 1.
   - `arithmatic_sequence_a(a, d, n)`: Returns the nth term of an arithmetic sequence. Enter 'a' as the first term, 'd' as the common difference, and 'n' as the term number.
   - `arithmatic_sequence_t(t, d, n)`: Returns the first term of an arithmetic sequence given the nth term 't', the common difference 'd', and the term number 'n'.

3. **Radicals**:
   - `simplify_radical(index, radicand)`: Simplifies a radical expression (like square roots). Provide the index (usually 2 for square roots) and the radicand (the number under the root).
   - `convert_to_entire_radical(index, coefficient, radicand)`: Converts a radical into an entire radical expression, combining the coefficient and radicand.
   - `combine_like_radicals(index, R_1, R_2, C_1, C_2)`: Combines like radicals by adding their coefficients and simplifying.

### How to use a function:
- Call a function by typing its name and passing the necessary values in parentheses. For example:
  - `vertex_quadratic(1, 0, 0)` to plot a quadratic equation in vertex form with 'a=1', 'p=0', and 'q=0'.
  - `quadratic_formula(1, -3, 2)` to calculate the roots of `x^2 - 3x + 2 = 0`.

If you're new to Python, make sure you have installed the required libraries (like `matplotlib`, `numpy`, and `sympy`). You can install them by typing the following command into command prompt:
    pip install matplotlib numpy sympy 
Happy Mathing!
"""


# Quadratics 
# Vertex Form
def vertex_quadratic(a=1,p=0,q=0):
    x = np.arange(-100,100,.001)
    y = a*(x-p)**2+q
    plt.plot(x, y)
    plt.axis([-10,10,-10,10])
    plt.show()
# Standard Form
def standard_quadratic(a=1, b=0, c=0):
    x = np.arange(-100,100,.001)
    y = a*x**2 + b*x + c
    plt.plot(x, y)
    plt.axis([-10,10,-10,10])
    plt.show()
# Factored Form
def factored_quadratic(a, X_1, X_2):
    x = np.arange(-100,100,.001)
    y = a*(x-X_1)*(x-X_2)
    plt.plot(x, y)
    plt.axis([-10,10,-10,10])
    plt.show()
# Quadratic Formula
def quadratic_formula(a,b,c):
    X_1 = (-b + np.sqrt(b**2-4*a*c))/(2*a)
    X_2 = (-b - np.sqrt(b**2-4*a*c))/(2*a)
    return X_1, X_2

# Sequences and Series
# Geometric
def geometric_sequence(a, r, n):
    A_n = a * r ** (n-1)
    return A_n
def geometric_series_fin(a,r,n):
    if r != 1:
        S_n = a*((1-r**n)/(1-r))
    else: 
        print("Error: 'r' cannot be equal 1. (Division by 0 error)")
    
def geometric_series_infin(a,r,n):
    if abs(r) < 1:
        S_inf = a/(1-r)
    else: 
        print("Error: 'r' cannot be equal 1. (Division by 0 error)")
# Arithmatic
def arithmatic_sequence_a(a, d, n):
    A_n = a + d * (n-1)
    return A_n
def arithmatic_sequence_t(t,d,n):
    A_1 = t - d * (n-1)
    return A_1

# Functions and Equations
# Radicals
def simplify_radical(index, radicand):
    """
    Simplifies a square root (radical) into its simplest form.
    For example, simplify_radical(72) returns (6, 2), representing 6√2.
    """
    for i in range(int(math.sqrt(index)), 0, -1):  # Start from √n and go down
        if radicand % (i ** index) == 0:  # Check if i² is a factor of n
            perfect_square = i ** index
            outside = i
            inside = radicand // perfect_square
            return outside, inside 
    
    print("No further simplification is possible")
    return 1, radicand
def convert_to_entire_radical(index, coefficent, radicand):
    combined = coefficent^index + radicand
    return str("Square Root of ({combined})"), np.sqrt(combined)

def combine_like_radicals(index, R_1, R_2, C_1 = 1, C_2 = 1):
    None, rad_1 = convert_to_entire_radical(index,C_1,R_1)
    None, rad_2 = convert_to_entire_radical(index,C_2,R_2)
    rad_sum = (rad_1 + rad_2) ** 2
    output = simplify_radical(rad_sum)
    return(output)