def apply(func, x, y):
    return func(x, y)

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

x = 15
y = 25
result1 = apply(add_numbers, x, y)
result2 = apply(multiply_numbers, x, y)
print(f"Addition result: {result1}")
print(f"Multiplication result: {result2}")
