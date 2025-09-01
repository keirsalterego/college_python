def find_larger(comparison_func, a, b):
    if comparison_func(a, b):
        return a
    else:
        return b

def greater_than(x, y):
    return x > y

num1 = 45
num2 = 32
larger = find_larger(greater_than, num1, num2)
print(f"Larger number between {num1} and {num2} is: {larger}")
