# Task 1: Convert lowercase letters to uppercase using ASCII

# Create array of small letters
letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]

# Convert using ASCII logic
capital_letters = []

for ch in letters:
    capital_letters.append(chr(ord(ch) - 32))

# Print result
print("Input (small letters):")
print(", ".join(letters))
print("\nOutput (capital letters):")
print(", ".join(capital_letters))