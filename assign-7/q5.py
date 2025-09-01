def is_palindrome(word):
    return word.lower() == word.lower()[::-1]

test_word1 = "madam"
test_word2 = "ravi"
print(f"'{test_word1}' is palindrome: {is_palindrome(test_word1)}")
print(f"'{test_word2}' is palindrome: {is_palindrome(test_word2)}")
