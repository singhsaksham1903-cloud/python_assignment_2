def even_numbers(limit):
    """Yields all even numbers up to the given limit."""
    for num in range(0, limit + 1, 2):
        yield num

# Using the generator to print even numbers up to 10
for number in even_numbers(10):
    print(number)
