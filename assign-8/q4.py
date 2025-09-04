with open("search_file.txt", "w") as file:
    file.write("Python is great\nI love Python programming\nJava is also good\nPython makes coding easy")

word = input("Enter word to search: ")

with open("search_file.txt", "r") as file:
    lines = file.readlines()
    
found = False
for i, line in enumerate(lines, 1):
    if word in line:
        print(f"Found '{word}' at line {i}")
        found = True

if not found:
    print(f"Word '{word}' not found in file")
