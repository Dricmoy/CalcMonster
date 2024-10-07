import sympy as sp

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
error_at_n = error_expr.subs(n, n_value)
print(f"Error at n = {n_value}: {error_at_n}")
