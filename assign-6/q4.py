
fruits = {
    "apple": 50,
    "banana": 20,
    "orange": 35,
    "mango": 60
}

print("Original fruits dictionary:")
for fruit, price in fruits.items():
    print(f"{fruit}: ₹{price}")


if "banana" in fruits:
    del fruits["banana"]
    print("\nAfter removing 'banana':")
    for fruit, price in fruits.items():
        print(f"{fruit}: ₹{price}")
else:
    print("\n'banana' not found in the dictionary")
