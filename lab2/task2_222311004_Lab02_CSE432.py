# Task 2: Symmetric Cipher (Caesar Cipher)

def encrypt(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                base = ord('A')
            else:
                base = ord('a')

            # Caesar Cipher logic
            keyed_char = chr((ord(ch) - base + key + 26) % 26 + base)
            result += keyed_char
        else:
            result += ch  # keep non-letters unchanged

    return result

def decrypt(cipher_text, key):
    return encrypt(cipher_text, -key)  # reverse shift

# Input
plain_text = input("Write a message: ")
key_value = int(input("Enter a secret key: "))

# Process
encrypted_text = encrypt(plain_text, key_value)
decrypted_text = decrypt(encrypted_text, key_value)

# Output
print("Original Text:", plain_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)