def reverse_cipher(text):
    """
    Applies the Reverse cipher to the input text

    Args:
        text (str): The text to be encrypted.

    Returns:
        str: The encrypted text using the Reverse cipher.
    """
    reversed_text = ""
    i = len(text) - 1
    while i >= 0:
        reversed_text = reversed_text + text[i]
        i -= 1
    return reversed_text


text = str(input("Type your text: "))


print(f"Plain text: {text}")
print(f"Cipher text: {reverse_cipher(text)}")