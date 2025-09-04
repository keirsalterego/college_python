with open("search_text.txt", "w") as file:
    file.write("Python is powerful\nI enjoy Python coding\nJava is different\nPython is easy to learn")

word = input("Enter word to search: ")

with open("search_text.txt", "r") as file:
    lines = file.readlines()

line_numbers = []
for i, line in enumerate(lines, 1):
    if word in line:
        line_numbers.append(i)

if line_numbers:
    print(f"Word '{word}' found at line numbers: {line_numbers}")
else:
    print(f"Word '{word}' not found")
