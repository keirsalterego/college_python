# Given string
sentence = "Python is fun and Python is powerful"

words = sentence.split()

word_freq = {}


for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Print the word frequencies
print("Word frequencies:")
for word, count in word_freq.items():
    print(f"{word}: {count}")

