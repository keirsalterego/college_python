def calculator():
    def addition(a, b):
        return a + b
    
    def subtraction(a, b):
        return a - b
    
    def multiplication(a, b):
        return a * b
    
    def division(a, b):
        return a / b if b != 0 else "Cannot divide by zero"
    
    return addition, subtraction, multiplication, division

add, sub, mul, div = calculator()
a = 20
b = 5
print(f"Addition: {add(a, b)}")
print(f"Subtraction: {sub(a, b)}")
print(f"Multiplication: {mul(a, b)}")
print(f"Division: {div(a, b)}")
