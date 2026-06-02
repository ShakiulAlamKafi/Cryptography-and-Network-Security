import random

def generate_private_key(p):
    """Generates a private key randomly chosen between 2 and p-2."""
    return random.randint(2, p - 2)

def generate_public_key(private_key, g, p):
    """Calculates the public key: (g ^ private_key) mod p."""
    return pow(g, private_key, p)

def calculate_shared_secret(their_public_key, my_private_key, p):
    """Calculates the shared secret: (their_public_key ^ my_private_key) mod p."""
    return pow(their_public_key, my_private_key, p)

if __name__ == "__main__":
    # 1. Publicly known parameters
    # Note: In a real-world scenario, 'p' would be a securely generated prime 
    # of at least 2048 bits, and 'g' is usually 2 or 5.
    p = 23  # Small prime modulus for demonstration
    g = 5   # Generator

    print("--- Public Parameters ---")
    print(f"Prime (p): {p}")
    print(f"Generator (g): {g}\n")

    # 2. Alice generates her keys
    alice_private = generate_private_key(p)
    alice_public = generate_public_key(alice_private, g, p)
    
    print("--- Alice's Keys ---")
    print(f"Private Key (a): {alice_private}")
    print(f"Public Key (A): {alice_public}\n")

    # 3. Bob generates his keys
    bob_private = generate_private_key(p)
    bob_public = generate_public_key(bob_private, g, p)

    print("--- Bob's Keys ---")
    print(f"Private Key (b): {bob_private}")
    print(f"Public Key (B): {bob_public}\n")

    # 4. Exchange public keys and calculate shared secret
    # Alice receives 'bob_public' (B)
    alice_shared_secret = calculate_shared_secret(bob_public, alice_private, p)
    
    # Bob receives 'alice_public' (A)
    bob_shared_secret = calculate_shared_secret(alice_public, bob_private, p)

    print("--- Shared Secret Calculation ---")
    print(f"Alice calculates: {alice_shared_secret}")
    print(f"Bob calculates: {bob_shared_secret}")

    # Verify that they match
    if alice_shared_secret == bob_shared_secret:
        print("\nSuccess! Both parties share the same secret.")
    else:
        print("\nError! The shared secrets do not match.")