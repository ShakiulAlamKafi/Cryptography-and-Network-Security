import random

def lehmann_prime_test(p, t):
    if p <= 2:
        print("p must be greater than 2")

    for _ in range(t):
        a = random.randint(2, p -1)
        e = int((p - 1) // 2)

        result = pow(a, e, p)

        if result != 1 and result != p - 1:
            return False

    return True

num = int(input("Enter a number: "))

lehmann_result = lehmann_prime_test(num, 10)

if lehmann_result:
    print(f"{num} is probably prime")
else:
    print(f"{num} is composite")