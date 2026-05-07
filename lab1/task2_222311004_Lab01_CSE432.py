# Task 2: Extract primes into another array
def sieve_of_eratosthenes(N):
    prime = list(range(N + 1))
    prime[0] = 0
    prime[1] = 0

    for i in range(2, int(N**0.5) + 1):
        if prime[i] != 0:
            for j in range(i * i, N + 1, i):
                prime[j] = 0

    return prime

# Input
N = int(input("Enter N: "))

# Get sieve result
prime = sieve_of_eratosthenes(N)

# Extract only primes
only_primes = []

for i in range(2, N + 1):
    if prime[i] != 0:
        only_primes.append(prime[i])

# Print result
print("Only primes array:")
for index, value in enumerate(only_primes):
    print(f"Index {index} -> Value {value}")