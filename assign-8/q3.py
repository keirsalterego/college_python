with open("sample.txt", "w") as file:
    file.write("Hello world\nThis is a test file\nWith multiple lines")

with open("sample.txt", "r") as file:
    content = file.read()
    
words = len(content.split())
characters = len(content)
lines = content.count('\n') + 1

print(f"Words: {words}")
print(f"Characters: {characters}")
print(f"Lines: {lines}")
