with open("test_file.txt", "w") as file:
    file.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5")

with open("test_file.txt", "r") as file:
    lines = file.readlines()
    
print(f"Number of lines: {len(lines)}")
