def find_unique_numbers(numbers):
    # Simpler approach
    return list(set(numbers))

large_list = [1, 2, 3, 4, 5] * 100000  # Large list of numbers
print(find_unique_numbers(large_list))
