try:
    age = int(input("Enter your age: "))
    
    if age < 18:
        raise ValueError("Age must be 18 or above.")
        
    print(f"Your age is {age}. Access granted!")
    
except ValueError as e:
    print(f"Error: {e}")
