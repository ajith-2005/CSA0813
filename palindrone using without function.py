def palindrome(word):
    return word == word[::-1]

input_word = "Hell0"
if palindrome(input_word):
    print(f"{input_word} is a palindrome!")
else:
    print(f"{input_word} is not a palindrome.")
