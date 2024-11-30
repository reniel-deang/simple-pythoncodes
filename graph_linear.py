# Install first scipy by running 'pip install scipy'
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def solve_linear_equations():
    # Input coefficients for the two equations
    print("For equation 1 (a1*x + b1*y = c1):")
    a1 = float(input("Enter coefficient a1: "))
    b1 = float(input("Enter coefficient b1: "))
    c1 = float(input("Enter constant c1: "))

    print("\nFor equation 2 (a2*x + b2*y = c2):")
    a2 = float(input("Enter coefficient a2: "))
    b2 = float(input("Enter coefficient b2: "))
    c2 = float(input("Enter constant c2: "))

    # Solve equation 1 for x
    if a1 != 0:
        print("\nSolving equation 1 for x:")
        # x = (c1 - b1*y) / a1
        x_expr = lambda y: (c1 - b1 * y) / a1
        # Substitute x_expr into equation 2: a2 * x_expr(y) + b2 * y = c2
        equation2_substituted = lambda y: a2 * x_expr(y) + b2 * y - c2
    else:
        print("\nSolving equation 1 for y:")
        # y = (c1 - a1*x) / b1
        y_expr = lambda x: (c1 - a1 * x) / b1
        # Substitute y_expr into equation 2: a2 * x + b2 * y_expr(x) = c2
        equation2_substituted = lambda x: a2 * x + b2 * y_expr(x) - c2

    # Use scipy to solve for y (or x if a1 == 0)
    if a1 != 0:
        y_solution = fsolve(equation2_substituted, 0)[0]
        x_solution = x_expr(y_solution)
    else:
        x_solution = fsolve(equation2_substituted, 0)[0]
        y_solution = y_expr(x_solution)

    print(f"\nSolution: x = {x_solution}, y = {y_solution}")

    # Now plot the solution on a Cartesian plane
    plot_solution(x_solution, y_solution)

def plot_solution(x, y):
    # Initialize the figure
    plt.axhline(0, color='black',linewidth=0.5)  # X-axis
    plt.axvline(0, color='black',linewidth=0.5)  # Y-axis
    plt.grid(True, which='both')  # Gridlines

    # Plot the point (x, y)
    plt.scatter([x], [y], color='red', marker='o', s=100)  # Red dot for the solution

    # Ensure the plane is centered around (0, 0) with some margin
    max_range = max(abs(x), abs(y))
    plt.xlim(-max_range - 1, max_range + 1)
    plt.ylim(-max_range - 1, max_range + 1)

    # Set labels and title
    plt.title(f"Solution at (x = {x}, y = {y})")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    # Show the plot
    plt.show()

# Run the function to solve the equations and plot the result
solve_linear_equations()
