from functools import reduce

strings = ["namaste", " ", "dost", " ", "kaise", " ", "ho"]
concatenated_string = reduce(lambda x, y: x + y, strings)
print(f"Strings: {strings}")
print(f"Concatenated: {concatenated_string}")
