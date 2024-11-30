import matplotlib.pyplot as plt

def plot_cartesian():
    # Get number of points from user
    num_points = int(input("How many points do you want to plot? "))
    
    # Initialize lists for x and y coordinates
    x_values = []
    y_values = []
    
    # Get x and y coordinates from user
    for i in range(num_points):
        x = float(input(f"Enter x-coordinate for point {i+1}: "))
        y = float(input(f"Enter y-coordinate for point {i+1}: "))
        x_values.append(x)
        y_values.append(y)
    
    # Plot the points on the Cartesian plane
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True, which='both')
    
    # Adjust the limits to center the plane at (0, 0)
    max_range = max(max(abs(min(x_values)), max(x_values)), max(abs(min(y_values)), max(y_values)))
    plt.xlim(-max_range - 1, max_range + 1)
    plt.ylim(-max_range - 1, max_range + 1)

    # Plot the points and connect them with a line
    plt.plot(x_values, y_values, color='blue', marker='o', linestyle='-', markersize=6)

    # Set labels and title
    plt.title("Cartesian Plane")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    # Show the plot
    plt.show()

# Call the function to plot points
plot_cartesian()
