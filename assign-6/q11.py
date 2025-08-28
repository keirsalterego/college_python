
numbers = {10, 20, 30}
print("Original set:", numbers)

numbers.add(40)
numbers.add(50)
print("After adding 40 and 50:", numbers)

numbers.discard(20)  

print("After removing 20:", numbers)


print("Final set:", sorted(numbers))
