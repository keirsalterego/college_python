celsius_temperatures = [0, 20, 25, 30, 35, 40]
fahrenheit_temperatures = list(map(lambda c: (c * 9/5) + 32, celsius_temperatures))
print(f"Celsius: {celsius_temperatures}")
print(f"Fahrenheit: {fahrenheit_temperatures}")
