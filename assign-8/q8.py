with open("word_count.txt", "w") as file:
    file.write("Hello world this is a sample text file for counting words")

with open("word_count.txt", "r") as file:
    content = file.read()
    
words = content.split()
print(f"Number of words: {len(words)}")
