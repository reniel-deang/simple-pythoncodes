import matplotlib.pyplot as plt

# Function to solve the linear equation and plot the graph
def solve_and_plot():
    # Get the coefficients for the linear equation y = mx + c
    print("Solving the linear equation of the form y = mx + c")
    
    # Get m (slope) and c (y-intercept) from the user
    m = float(input("Enter the value of the slope (m): "))
    c = float(input("Enter the value of the y-intercept (c): "))

    # Ask for a specific range of x-values to plot
    x_min = float(input("Enter the minimum x value: "))
    x_max = float(input("Enter the maximum x value: "))
    
    # Create a range of x values
    x_values = [x for x in range(int(x_min), int(x_max) + 1)]
    
    # Calculate corresponding y values based on the equation y = mx + c
    y_values = [m * x + c for x in x_values]
    
    # Plot the graph on the Cartesian plane
    plt.axhline(0, color='black',linewidth=0.5)  # X-axis
    plt.axvline(0, color='black',linewidth=0.5)  # Y-axis
    plt.grid(True, which='both')  # Gridlines
    
    # Adjust limits to keep the plane centered around (0, 0)
    max_range = max(max(abs(min(x_values)), max(x_values)), max(abs(min(y_values)), max(y_values)))
    plt.xlim(-max_range - 1, max_range + 1)
    plt.ylim(-max_range - 1, max_range + 1)

    # Plot the line based on the equation y = mx + c
    plt.plot(x_values, y_values, color='blue', marker='o', linestyle='-', markersize=6, label=f'y = {m}x + {c}')

    # Add labels and title
    plt.title("Graph of y = mx + c")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    # Show the equation as a label
    plt.legend()

    # Show the graph
    plt.show()

# Call the function
solve_and_plot()
