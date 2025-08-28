
student = {
    "name": "Manish",
    "age": 20,
    "branch": "CSE"
}

print("Original student details:")
for key, value in student.items():
    print(f"{key}: {value}")


student["age"] = 21
student["grade"] = "A"

print("\nUpdated student details:")
for key, value in student.items():
    print(f"{key}: {value}")
