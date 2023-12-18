def caesar_cipher(text, shift):
    """
    Applies the Caesar cipher to the input text

    Args:
        text (str): The text to be encrypted.
        shift (int): The number of positions to shift each character.

    Returns:
        str: The encrypted text using the Caesar cipher.
    """

    result = ""
    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            # Shift uppercase letters and wrap within the range of 'A' to 'Z'
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            # Shift lowercase letters and wrap within the range of 'a' to 'z'
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result


text = str(input("Type your text: "))
shift = int(input("Type your shift: "))

print(f"Plain text: {text}")
print(f"Shift pattern: {shift}")
print(f"Cipher: {caesar_cipher(text, shift)}")