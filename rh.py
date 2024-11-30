import numpy as np

def routh_hurwitz(coefficients):
    """Calculates the Routh array and checks system stability."""
    n = len(coefficients)
    # Number of rows in Routh array
    rows = (n + 1) // 2
    routh_array = np.zeros((n, rows))

    # Fill the first two rows
    routh_array[0, :len(coefficients[::2])] = coefficients[::2]  # Even coefficients
    routh_array[1, :len(coefficients[1::2])] = coefficients[1::2]  # Odd coefficients

    # Fill the rest of the Routh array
    for i in range(2, n):
        for j in range(rows - 1):
            try:
                numerator = (routh_array[i - 1, 0] * routh_array[i - 2, j + 1] -
                             routh_array[i - 2, 0] * routh_array[i - 1, j + 1])
                denominator = routh_array[i - 1, 0]
                routh_array[i, j] = numerator / denominator if denominator != 0 else 0
            except IndexError:
                pass

        # Special case: If the first element of a row is zero, replace it with a small epsilon
        if np.all(routh_array[i, :] == 0):  # Entire row is zero (special case)
            for j in range(rows - 1):
                routh_array[i, j] = (routh_array[i - 2, j + 1] - routh_array[i - 2, 0])
        elif routh_array[i, 0] == 0:
            routh_array[i, 0] = 1e-4

    # Check for stability
    first_column = routh_array[:, 0]
    is_stable = np.all(first_column > 0)

    return routh_array, is_stable

def main():
    print("Routh-Hurwitz Stability Criterion Calculator")
    order = int(input("Enter the order of the system: "))
    
    print(f"Enter the coefficients of the characteristic equation (highest to lowest order):")
    coefficients = []
    for i in range(order + 1):
        coeff = float(input(f"Coefficient of s^{order - i}: "))
        coefficients.append(coeff)

    print("\nSolving using Routh-Hurwitz Stability Criterion...\n")
    routh_array, is_stable = routh_hurwitz(coefficients)
    
    print("Routh Array:")
    for row in routh_array:
        print(["{:.2f}".format(x) for x in row if x != 0])

    if is_stable:
        print("\nThe system is STABLE.")
    else:
        print("\nThe system is UNSTABLE.")

if __name__ == "__main__":
    main()
