def reverse_replace(text):
    # Traverse the text from right to left and construct a new string
    result = ""

    for char in reversed(text):
        result += char

    return result

# Ask for user input
text = input("Enter the text to be reversed: ")

# Reverse the text (replace characters from right to left)
reversed_text = reverse_replace(text)
print(f"Reversed Text: {reversed_text}")