try:
    with open("test_read.txt", "r") as file:
        content = file.read()
        print("File contents:")
        print(content)
        
except FileNotFoundError:
    print("Error: File not found!")
    
finally:
    print("File operation complete")
