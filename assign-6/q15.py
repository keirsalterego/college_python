# Given sentence
sentence = "I hate silicon"

words = sentence.lower().split()
unique_words = set(words)

unique_words_sorted = sorted(unique_words)

print("Unique words in the sentence:")
for word in unique_words_sorted:
    print(f"- {word}")

