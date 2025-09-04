with open("sample.txt", "w") as file:
    file.write("First line\nSecond line\nThird line\nFourth line")

with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())
