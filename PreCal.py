

# Quadratics 
# Vertex Form
def vertex_quadratic(a=1, p=0, q=0):
    """
    Plots a quadratic equation in vertex form: y = a(x-p)^2 + q.
    
    Parameters:
    a (float): The vertical stretch or compression factor.
    p (float): The horizontal shift (vertex's x-coordinate).
    q (float): The vertical shift (vertex's y-coordinate).
    
    Returns:
    None: Displays the plot of the quadratic function.
    """
    x = np.arange(-100, 100, .001)
    y = a * (x - p)**2 + q
    plt.plot(x, y)
    plt.axis([-10, 10, -10, 10])
    plt.show()

# Standard Form
def standard_quadratic(a=1, b=0, c=0):
    """
    Plots a quadratic equation in standard form: y = ax^2 + bx + c.
    
    Parameters:
    a (float): Coefficient of x^2.
    b (float): Coefficient of x.
    c (float): Constant term.
    
    Returns:
    None: Displays the plot of the quadratic function.
    """
    x = np.arange(-100, 100, .001)
    y = a * x**2 + b * x + c
    plt.plot(x, y)
    plt.axis([-10, 10, -10, 10])
    plt.show()

# Factored Form
def factored_quadratic(a, X_1, X_2):
    """
    Plots a quadratic equation in factored form: y = a(x-X_1)(x-X_2).
    
    Parameters:
    a (float): Leading coefficient.
    X_1 (float): First root of the quadratic equation.
    X_2 (float): Second root of the quadratic equation.
    
    Returns:
    None: Displays the plot of the quadratic function.
    """
    x = np.arange(-100, 100, .001)
    y = a * (x - X_1) * (x - X_2)
    plt.plot(x, y)
    plt.axis([-10, 10, -10, 10])
    plt.show()

# Quadratic Formula
def quadratic_formula(a, b, c):
    """
    Solves a quadratic equation: ax^2 + bx + c = 0 using the quadratic formula.
    
    Parameters:
    a (float): Coefficient of x^2.
    b (float): Coefficient of x.
    c (float): Constant term.
    
    Returns:
    tuple: Two solutions of the quadratic equation.
    """
    X_1 = (-b + np.sqrt(b**2 - 4 * a * c)) / (2 * a)
    X_2 = (-b - np.sqrt(b**2 - 4 * a * c)) / (2 * a)
    return X_1, X_2

# Sequences and Series
# Geometric
def geometric_sequence(a, r, n):
    """
    Finds the nth term of a geometric sequence: a * r^(n-1).
    
    Parameters:
    a (float): First term of the sequence.
    r (float): Common ratio.
    n (int): Term number.
    
    Returns:
    float: The nth term of the sequence.
    """
    A_n = a * r ** (n - 1)
    return A_n

def geometric_series_fin(a, r, n):
    """
    Calculates the sum of the first n terms of a geometric series.
    
    Parameters:
    a (float): First term of the series.
    r (float): Common ratio.
    n (int): Number of terms.
    
    Returns:
    float: Sum of the series if r ≠ 1.
    None: Prints an error message if r = 1.
    """
    if r != 1:
        S_n = a * ((1 - r**n) / (1 - r))
        return S_n
    else:
        print("Error: 'r' cannot be equal to 1. (Division by 0 error)")

# Sequences and Series
# Infinite Geometric Series
def geometric_series_infin(a, r):
    """
    Calculates the sum of an infinite geometric series if |r| < 1.
    
    Parameters:
    a (float): First term of the series.
    r (float): Common ratio.
    
    Returns:
    float: Sum of the series if |r| < 1.
    None: Prints an error message if |r| >= 1.
    """
    if abs(r) < 1:
        S_inf = a / (1 - r)
        return S_inf
    else:
        print("Error: |r| must be less than 1 for an infinite series.")

# Arithmetic Sequence
def arithmatic_sequence_a(a, d, n):
    """
    Finds the nth term of an arithmetic sequence: A_n = a + d * (n-1).
    
    Parameters:
    a (float): First term of the sequence.
    d (float): Common difference between consecutive terms.
    n (int): Term number.
    
    Returns:
    float: The nth term of the sequence.
    """
    A_n = a + d * (n - 1)
    return A_n

def arithmatic_sequence_t(t, d, n):
    """
    Finds the first term of an arithmetic sequence given the nth term.
    
    Parameters:
    t (float): The nth term of the sequence.
    d (float): Common difference between consecutive terms.
    n (int): Term number of the given nth term.
    
    Returns:
    float: The first term of the sequence.
    """
    A_1 = t - d * (n - 1)
    return A_1

# Radicals
def simplify_radical(index, radicand):
    """
    Simplifies a radical expression: index√(radicand).
    
    Parameters:
    index (int): The root's index (e.g., 2 for square root, 3 for cube root).
    radicand (int): The number under the root.
    
    Returns:
    tuple: The simplified radical as (outside, inside).
    """
    for i in range(int(math.sqrt(radicand)), 0, -1):
        if radicand % (i ** index) == 0:
            perfect_power = i ** index
            outside = i
            inside = radicand // perfect_power
            return outside, inside
    
    print("No further simplification is possible.")
    return 1, radicand

def convert_to_entire_radical(index, coefficient, radicand):
    """
    Converts a simplified radical into an entire radical expression.
    
    Parameters:
    index (int): The root's index (e.g., 2 for square root, 3 for cube root).
    coefficient (int): The number outside the radical.
    radicand (int): The number inside the radical.
    
    Returns:
    str: The entire radical as a string.
    """
    combined = (coefficient ** index) * radicand
    return f"{index}√({combined})", np.sqrt(combined)

def combine_like_radicals(index, R_1, R_2, C_1=1, C_2=1):
    """
    Combines like radicals by adding coefficients and simplifying.
    
    Parameters:
    index (int): The root's index (e.g., 2 for square root, 3 for cube root).
    R_1 (int): The radicand of the first radical.
    R_2 (int): The radicand of the second radical.
    C_1 (int, optional): Coefficient of the first radical. Default is 1.
    C_2 (int, optional): Coefficient of the second radical. Default is 1.
    
    Returns:
    tuple: The simplified combined radical as (outside, inside).
    """
    _, rad_1 = convert_to_entire_radical(index, C_1, R_1)
    _, rad_2 = convert_to_entire_radical(index, C_2, R_2)
    rad_sum = rad_1 + rad_2
    return simplify_radical(index, rad_sum)

# Rational Functions
def simplify_rational_functions(numerator, denominator):
    """
    Simplifies a rational function: numerator/denominator.
    
    Parameters:
    numerator (sympy expression): The numerator of the rational function.
    denominator (sympy expression): The denominator of the rational function.
    
    Returns:
    sympy expression: The simplified rational function.
    """
    simplified_function = simplify(numerator / denominator)
    return simplified_function
