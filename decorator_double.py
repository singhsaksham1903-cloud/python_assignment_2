def double_result(func):
    """A decorator that doubles the return value of a function."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

# Applying the decorator to the add function
@double_result
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

# Example usage
print(add(3, 5))  # Output: 16 (Since 3 + 5 = 8, and 8 * 2 = 16)
print(add(10, 2.5))  # Output: 25.0 (Since 10 + 2.5 = 12.5, and 12.5 * 2 = 25.0)