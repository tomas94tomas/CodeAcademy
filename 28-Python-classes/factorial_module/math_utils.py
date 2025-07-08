def factorial(n):
    """Calculate factorial of n (n!) recursively."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)
