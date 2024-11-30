import numpy as np

def hurwitz_matrix(coeffs):
    """
    Function to create a Hurwitz matrix from the polynomial coefficients.
    Args:
        coeffs (list): Coefficients of the characteristic polynomial in descending order of powers.
    Returns:
        np.ndarray: Hurwitz matrix.
    """
    n = len(coeffs)  # Degree of the polynomial
    hurwitz = np.zeros((n, n))  # Initialize an n x n matrix with zeros
    
    for i in range(n):
        for j in range((n // 2) + 1):
            if 2 * j + i < n:
                hurwitz[i, j] = coeffs[2 * j + i]
    
    return hurwitz[:n-1, :]  # Return the square Hurwitz matrix


def is_stable(coeffs):
    """
    Function to check if the system is stable based on the Hurwitz matrix.
    Args:
        coeffs (list): Coefficients of the characteristic polynomial in descending order of powers.
    Returns:
        bool: True if stable, False otherwise.
    """
    hurwitz = hurwitz_matrix(coeffs)
    for i in range(len(hurwitz)):
        determinant = np.linalg.det(hurwitz[:i+1, :i+1])
        if determinant <= 0:
            return False
    return True


def main():
    print("Hurwitz Stability Matrix Calculator")
    print("Enter the coefficients of the characteristic polynomial in descending order of powers (e.g., for s^3 + 2s^2 + 3s + 4, input 1 2 3 4):")
    coeffs = list(map(float, input("Coefficients: ").split()))
    
    # Generate the Hurwitz matrix
    hurwitz = hurwitz_matrix(coeffs)
    print("\nHurwitz Matrix:")
    print(hurwitz)
    
    # Check stability
    if is_stable(coeffs):
        print("\nThe system is stable.")
    else:
        print("\nThe system is not stable.")

if __name__ == "__main__":
    main()
