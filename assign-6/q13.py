
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers_set = list(set(numbers))
print("Using set():", unique_numbers_set)

unique_numbers_ordered = list(dict.fromkeys(numbers))
print("Using dict.fromkeys() (order preserved):", unique_numbers_ordered)

unique_numbers_loop = []
for num in numbers:
    if num not in unique_numbers_loop:
        unique_numbers_loop.append(num)
print("Using loop (order preserved):", unique_numbers_loop)
