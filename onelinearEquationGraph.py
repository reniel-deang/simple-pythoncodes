import numpy as np
import matplotlib.pyplot as plt

def solve_and_plot_linear_equation():
    # Input coefficients for the linear equation
    print("For the equation (a1*x + b1*y = c1):")
    a1 = float(input("Enter coefficient a1: "))
    b1 = float(input("Enter coefficient b1: "))
    c1 = float(input("Enter constant c1: "))

    # Set the x and y range for the graph
    x_range = 10  # Controls the range of x-axis (e.g., from -10 to 10)
    y_range = 10  # Controls the range of y-axis (e.g., from -10 to 10)

    if b1 == 0:
        print("This equation represents a vertical line, as it is not solvable for y.")
        x = c1 / a1  # x is constant for a vertical line
        print(f"Equation is x = {x}")
        
        # Plot the vertical line
        x_vals = np.full(100, x)  # x is constant
        y_vals = np.linspace(-y_range, y_range, 100)  # Use the defined y range

        plt.plot(x_vals, y_vals, label=f'x = {x}')
    else:
        # Solve for y in terms of x: y = (c1 - a1*x) / b1
        def y_expr(x):
            return (c1 - a1 * x) / b1

        # Generate x values
        x_vals = np.linspace(-x_range, x_range, 100)  # Use the defined x range
        y_vals = y_expr(x_vals)

        # Plot the equation
        plt.plot(x_vals, y_vals, label=f'{a1}x + {b1}y = {c1}')

    # Graph setup
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, which='both')

    # Set x and y axis limits to keep (0, 0) at the center
    plt.xlim(-x_range, x_range)
    plt.ylim(-y_range, y_range)

    # Set the x and y axis labels
    plt.xlabel('x')
    plt.ylabel('y')
    
    # Set title
    plt.title(f"Graph of {a1}x + {b1}y = {c1}")

    # Force x and y ticks to be whole numbers
    plt.xticks(np.arange(-x_range, x_range + 1, 1))  # Set x ticks to whole numbers
    plt.yticks(np.arange(-y_range, y_range + 1, 1))  # Set y ticks to whole numbers

    # Show legend
    plt.legend()

    # Show plot
    plt.show()

# Run the function
solve_and_plot_linear_equation()
