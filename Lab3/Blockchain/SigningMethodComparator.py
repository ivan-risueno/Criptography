from time import time
from BlockChainRSA import *
from hashlib import sha256


if __name__ == "__main__":
    f = open("./ComparisonTable.csv", "w")

    bits_mod = [512, 1024, 2048, 4096]
    messages = [int(sha256(f"Sign #{0}".encode()).hexdigest(), 16) for i in range(100)]

    f.write("Bits,TCR,No TCR\n")

    for mod in bits_mod:
        rsa = rsa_key(mod)
        f.write(str(mod) + ",")

        t0 = time()
        for message in messages:
            rsa.sign(message)

        t1 = time()
        for message in messages:
            rsa.sign_slow(message)

        t2 = time()
        f.write(str(t1-t0) + "," + str(t2-t1) + '\n')
