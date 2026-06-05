import random;

def diffie_hellman(prime, primitive_root):
    XA = random.randint(1, prime - 1)
    #XA=4
    YA = pow(primitive_root, XA, prime)
    print(f"A's private key is {XA} & public key is {YA}")

    XB =  random.randint(1, prime - 1)
    #XB=3
    YB = pow(primitive_root, XB, prime)
    print(f"B's private key is {XB} & public key is {YB}")

    SA = pow(YB, XA, prime)
    SB = pow(YA, XB, prime)

    print(f"The common key generated at A's end is {SA} & B's end is {SB}")

    if SA==SB:
        print("\nSuccess! Both parties share the same secret.")
    else:
        print("\nError! The shared secrets do not match.")

prime = 7
primitive_root = 3
diffie_hellman(prime, primitive_root)