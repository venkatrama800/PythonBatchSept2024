#!/usr/bin/python3
"""
Purpose: Demonstration of Palindrome check

    palindrome strings
        dad
        mom

Algorithms:
-----------
Step 1: Take the string in run-time and store in a variable


"""

input_word= input("Enter word: ")

# To Print the result directly using a ternary expression
print(f"'{input_word}' is a palindrome." if input_word == input_word[::-1] else f"'{input_word}' is not a palindrome.")