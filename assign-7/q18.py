def power_of(x):
    def power_func(n):
        return n ** x
    return power_func

power_of_2 = power_of(2)
power_of_3 = power_of(3)

number = 4
result1 = power_of_2(number)
result2 = power_of_3(number)
print(f"{number} to the power of 2: {result1}")
print(f"{number} to the power of 3: {result2}")
