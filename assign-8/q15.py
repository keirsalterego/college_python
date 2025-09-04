try:
    filename = input("Enter filename: ")
    user_input = input("Enter text to write to file: ")
    
    with open(filename, "w") as file:
        file.write(user_input)
        
    print(f"Successfully wrote to {filename}")
    
except IOError:
    print("Error: Cannot open or write to file. Check file path and permissions.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
