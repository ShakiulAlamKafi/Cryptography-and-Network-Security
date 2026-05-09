import string

plain_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher_alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"  # fixed key


def encrypt(text):
    result = ""

    for ch in text:
        if ch.isalpha():
            is_upper = ch.isupper()
            upper_char = ch.upper()

            index = plain_alphabet.index(upper_char)
            encrypted_char = cipher_alphabet[index]

            if not is_upper:
                encrypted_char = encrypted_char.lower()

            result += encrypted_char
        else:
            result += ch

    return result


def decrypt(cipher_text):
    result = ""

    for ch in cipher_text:
        if ch.isalpha():
            is_upper = ch.isupper()
            upper_char = ch.upper()

            index = cipher_alphabet.index(upper_char)
            decrypted_char = plain_alphabet[index]

            if not is_upper:
                decrypted_char = decrypted_char.lower()

            result += decrypted_char
        else:
            result += ch

    return result


text = input("Enter text: ")

encrypted = encrypt(text)
decrypted = decrypt(encrypted)

print("Original:", text)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)