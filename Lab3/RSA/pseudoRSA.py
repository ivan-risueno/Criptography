from Crypto.PublicKey import RSA
from sympy import isprime, gcd
import math
import os

STUDENTS = ["ivan.risueno", "miguel.moreno.alcaraz"]  # name.surname1(.surname2)

for student in STUDENTS:
    os.system("openssl rsa -in ./inputs/" + student + "_pubkeyRSA_pseudo.pem -pubin -text -modulus > salida.txt")

    f = open("salida.txt", "r")
    op = f.read()
    mida = int(op[13:18])
    inicio = op.find("Modulus=") + len("Modulus=")
    final = op.find("\n", inicio)

    n = int(op[inicio:final], 16)
    f.close()

    nbits = 2048
    base = nbits // 4
    b = pow(2, base)

    a = int(n)
    res = [0 for _ in range(4)]
    i = 3
    while a > 0:
        res[i] = a % b
        a = a >> base
        i = i - 1

    rsl = res[3]
    p = -1
    q = -1
    for carry in range(3):
        rsh = res[0] - carry
        rs = b * rsh + rsl
        aux = b * res[1] + res[2] + carry * b * b - rsl * b - rsh
        aux = aux + 2 * rs
        sumrs = math.isqrt(aux)

        if sumrs * sumrs != aux:
            continue

        sqr = math.isqrt(aux - 4 * rs)

        r = (sumrs + sqr) // 2
        s = (sumrs - sqr) // 2

        print("R:" + str(r))
        print("S:" + str(s))

        p = b * r + s
        q = b * s + r

        if int(n) == p * q:
            print(student + "'s p: " + str(p))
            print(student + "'s q: " + str(q))

    mod = int(n)
    e = 65537

    # Calculate the private exponent(d) at: https://www.tausquared.net/pages/ctf/rsa.html
    d = int(input("Enter the private exponent(d) obtained in base 10: "))
    print("Validating RSA mathematical restrictions...")
    assert (isprime(p))
    assert (isprime(q))
    assert (p * q == mod)
    assert (gcd(e, (p - 1) * (q - 1)) == 1)

    thistuple = (mod, e, d, p, q)
    key = RSA.construct(thistuple, True)
    f = open("./outputs/pseudoRSA/" + student + "_privatekey_pseudoRSA.pem", 'wb')
    f.write(key.export_key('PEM'))
    f.close()

    os.system(
        "openssl rsautl -decrypt -in ./inputs/" + student + "_RSA_pseudo.enc -out "
        "./outputs/pseudoRSA/" + student + "_decrypted_pseudoRSA.txt -inkey "
        "./outputs/pseudoRSA/" + student + "_privatekey_pseudoRSA.pem")
    os.system(
        "openssl aes-128-cbc -pbkdf2 -d -kfile ./outputs/pseudoRSA/" + student + "_decrypted_pseudoRSA.txt  -in "
        "./inputs/" + student + "_AES_pseudo.enc -out ./outputs/pseudoRSA/" + student + "_psuedoRSA.png -p")
