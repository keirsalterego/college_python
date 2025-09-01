words = ["ravi", "suresh", "kavitha", "raj", "sanjana", "mahesh", "divya"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(f"All words: {words}")
print(f"Words longer than 5 characters: {long_words}")
