import sympy as sp
import numpy as np

def S_n(n):
    return 2 * np.sqrt(3) * sum((-1)**k / (3**k * (2*k + 1)) for k in range(n + 1))

# Define the symbol and error expression
n = sp.symbols('n', integer=True)
error_expr = 1 / (3**(n+1) * (2*(n+1) + 1))

# Set the tolerance
tolerance = 10**(-3)

# Find the smallest n such that the error is less than 10^-3
n_value = 0  # Start from n=0
while error_expr.subs(n, n_value) >= tolerance:
    n_value += 1

# Print the value of n
print(f"The smallest n such that the error is less than 10^-3 is: {n_value}")

# Test the value of n by substituting it back into the error expression
error_at_n = error_expr.subs(n, 4)
print(f"Error at n = {n_value}: {error_at_n}")


# Compute the partial sum for n=4
n = 4
S4 = S_n(n)
print(f"Partial sum S_4: {S4}")

