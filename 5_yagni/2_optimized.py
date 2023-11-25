def find_unique_numbers(numbers):
    # Using a set for optimization
    unique_numbers = set()
    for number in numbers:
        unique_numbers.add(number)
    return list(unique_numbers)

large_list = [1, 2, 3, 4, 5] * 100000  # Large list of numbers
print(find_unique_numbers(large_list))
