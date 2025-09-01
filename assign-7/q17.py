def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

multiply_by_3 = make_multiplier(3)
multiply_by_7 = make_multiplier(7)

number = 8
result1 = multiply_by_3(number)
result2 = multiply_by_7(number)
print(f"{number} multiplied by 3: {result1}")
print(f"{number} multiplied by 7: {result2}")
