def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Shift character, preserving case (upper or lower)
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            # If it's not a letter, leave it unchanged
            result += char

    return result

# Ask for user input
text = input("Enter the text to be encrypted: ")  # This will prompt for input
shift = 3  # Fixed shift of +3 for Caesar cipher

# Encrypt the text
encrypted_text = caesar_cipher(text, shift)
print(f"Encrypted Text: {encrypted_text}")