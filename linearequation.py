# Install first scipy by running 'pip install scipy'
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import numpy as np

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

    # Define the system of equations
    def equations(vars):
        x, y = vars
        eq1 = a1 * x + b1 * y - c1
        eq2 = a2 * x + b2 * y - c2
        return [eq1, eq2]

    # Solve the system
    x_solution, y_solution = fsolve(equations, (0, 0))

    print(f"\nSolution: x = {x_solution}, y = {y_solution}")

    # Plot the lines and the solution point
    plot_solution(x_solution, y_solution, a1, b1, c1, a2, b2, c2)

def plot_solution(x, y, a1, b1, c1, a2, b2, c2):
    # Generate x values for plotting lines
    x_values = np.linspace(x - 10, x + 10, 400)

    # Calculate y values for both lines
    if b1 != 0:
        y_values_line1 = (c1 - a1 * x_values) / b1
    else:
        x_values_line1 = np.full_like(x_values, c1 / a1)
        y_values_line1 = x_values  # Dummy y values for a vertical line

    if b2 != 0:
        y_values_line2 = (c2 - a2 * x_values) / b2
    else:
        x_values_line2 = np.full_like(x_values, c2 / a2)
        y_values_line2 = x_values  # Dummy y values for a vertical line

    # Initialize the figure
    plt.axhline(0, color='black', linewidth=0.5)  # X-axis
    plt.axvline(0, color='black', linewidth=0.5)  # Y-axis
    plt.grid(True, which='both')  # Gridlines

    # Plot the lines
    if b1 != 0:
        plt.plot(x_values, y_values_line1, label=f"{a1}*x + {b1}*y = {c1}", color='blue')
    else:
        plt.plot(x_values_line1, y_values_line1, label=f"{a1}*x + {b1}*y = {c1}", color='blue')

    if b2 != 0:
        plt.plot(x_values, y_values_line2, label=f"{a2}*x + {b2}*y = {c2}", color='green')
    else:
        plt.plot(x_values_line2, y_values_line2, label=f"{a2}*x + {b2}*y = {c2}", color='green')

    # Plot the intersection point (x, y)
    plt.scatter([x], [y], color='red', marker='o', s=100, label="Intersection")  # Red dot for the solution

    # Ensure the plane is centered around (0, 0) with some margin
    max_range = max(abs(x), abs(y)) + 1
    plt.xlim(-max_range, max_range)
    plt.ylim(-max_range, max_range)

    # Set labels and title
    plt.title(f"Generated Graph Based on Linear Equation")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()

    # Show the plot
    plt.show()

# Run the function to solve the equations and plot the result
solve_linear_equations()
