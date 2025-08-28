
book = {
    "title": "Python Programming",
    "author": "John Smith",
    "price": 599.99
}


print("Book Details:")
for key, value in book.items():
    print(f"{key.capitalize()}: {value}")
