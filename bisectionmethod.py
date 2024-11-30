import sympy as sp

def bisection_method(func, a, b, tolerance=1e-6, max_iterations=100):
    """
    Find a root of a function using the bisection method.
    
    Parameters:
    func: A lambda function representing the equation.
    a, b: The interval [a, b].
    tolerance: Stopping criteria for the root.
    max_iterations: Maximum number of iterations allowed.
    
    Returns:
    A root of the equation if found, or None if no root exists in the interval.
    """
    if func(a) * func(b) > 0:
        print("The function does not change sign in the interval. No root found.")
        return None
    
    iteration = 0
    while iteration < max_iterations:
        c = (a + b) / 2
        f_c = func(c)
        
        if abs(f_c) < tolerance or (b - a) / 2 < tolerance:
            return c
        
        if func(a) * f_c < 0:
            b = c
        else:
            a = c
        
        iteration += 1
    
    print("Maximum iterations reached. No root found.")
    return None


# Main program
def main():
    print("Root Finding Using Bisection Method")
    equation_input = input("Enter the equation in terms of x (e.g., x**3 - 4*x - 9): ")
    a = float(input("Enter the start of the interval (a): "))
    b = float(input("Enter the end of the interval (b): "))
    
    # Define the variable and parse the equation
    x = sp.symbols('x')
    equation = sp.sympify(equation_input)
    f = sp.lambdify(x, equation)
    
    # Solve using the bisection method
    root = bisection_method(f, a, b)
    if root is not None:
        print(f"A root is approximately: {root}")
    else:
        print("No root found in the given interval.")

if __name__ == "__main__":
    main()
