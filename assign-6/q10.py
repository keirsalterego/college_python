
students = {101: "Amit", 102: "Riya", 103: "John"}

inverted_students = {name: roll for roll, name in students.items()}

print("Original dictionary:", students)
print("Inverted dictionary:", inverted_students)

