numbers = [10, 20, 30, 40, 50]

with open("number_list.txt", "w") as file:
    for num in numbers:
        file.write(str(num) + "\n")

with open("number_list.txt", "r") as file:
    lines = file.readlines()

result_list = []
for line in lines:
    result_list.append(int(line.strip()))

print(result_list)
