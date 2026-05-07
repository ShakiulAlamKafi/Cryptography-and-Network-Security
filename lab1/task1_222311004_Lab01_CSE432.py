# Task 1: Sieve of Eratosthenes
def sieve_of_eratosthenes(N):
    # Initialize array: prime[i] = i
    prime = list(range(N + 1))

    # Mark 0 and 1 as non-prime
    prime[0] = 0
    prime[1] = 0

    # Apply sieve
    for i in range(2, int(N**0.5) + 1):
        if prime[i] != 0:
            for j in range(i * i, N + 1, i):
                prime[j] = 0

    return prime

# Input
N = int(input("Enter N: "))

# Get sieve result
prime = sieve_of_eratosthenes(N)

# Print all prime numbers
print("Prime numbers:")
for i in range(2, N + 1):
    if prime[i] != 0:
        print(prime[i], end=" ")