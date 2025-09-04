numbers = [10, 20, 30, 40, 50]

with open("numbers.txt", "w") as file:
    for num in numbers:
        file.write(str(num) + "\n")

with open("numbers.txt", "r") as file:
    lines = file.readlines()
    
number_list = []
for line in lines:
    number_list.append(int(line.strip()))

print(number_list)
