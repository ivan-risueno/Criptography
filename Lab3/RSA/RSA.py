from Crypto.PublicKey import RSA
from sympy import gcd
from sympy import isprime
import os

STUDENTS = ["ivan.risueno", "miguel.moreno.alcaraz"]  # name.surname1(.surname2)

os.system("cd inputs && ls *_RW.pem > ../outputs/llista.txt && cd ..")

ll = open("outputs/llista.txt", "r")
l = ll.readlines()

mods = [0 for _ in range(len(l))]
common_mods = [0 for _ in range(len(l))]

i = 0
for item in l:
    print(item.strip())
    s = "openssl rsa -in " + "inputs/" + item.strip() + " -pubin -text -modulus > outputs/salida.txt"
    os.system(s)
    f = open("outputs/salida.txt", "r")
    op = f.read()
    mida = int(op[13:18])
    inicio = op.find("Modulus=") + len("Modulus=")
    final = op.find("\n", inicio)

    mods[i] = int(op[inicio:final], 16)
    f.close()
    i = i + 1

indices = []
with open("outputs/llista.txt", "r") as f:
    for line_number, line in enumerate(f, start=1):
        for student in STUDENTS:
            if line.startswith(student):
                indices.append(line_number - 1)


for i in range(0, len(STUDENTS)):
    student_index = indices[i]
    final = student_index
    for j in range(len(mods)):
        aux = gcd(mods[j], mods[student_index])
        common_mods[j] = aux
        if aux != 1 and j != student_index:
            final = j

    n = mods[student_index]
    p = common_mods[final]
    q = n / p

    print(STUDENTS[i] + "'s p: " + str(p))
    print(STUDENTS[i] + "'s q: " + str(q))
    mod = n
    e = 65537

    # Calculate the private exponent(d) at: https://www.tausquared.net/pages/ctf/rsa.html
    d = int(input("Enter the private exponent(d) obtained in base 10: "))
    print("Validating RSA mathematical restrictions...")
    p = int(p)
    q = int(q)
    assert (isprime(p))
    assert (isprime(q))
    assert (p * q == mod)
    assert (gcd(e, (p - 1) * (q - 1)) == 1)

    thistuple = (mod, e, int(d), p, q)
    key = RSA.construct(thistuple, True)

    f = open("outputs/RSA/" + STUDENTS[i] + "_privatekey_RSA.pem", 'wb')
    f.write(key.export_key('PEM'))
    f.close()

    os.system("openssl rsautl -decrypt -in inputs/" + STUDENTS[i] + "_RSA_RW.enc -out outputs/RSA/" + STUDENTS[i] + "_decrypted_RSA.txt -inkey outputs/RSA/" + STUDENTS[i] + "_privatekey_RSA.pem")
    os.system("openssl aes-128-cbc -pbkdf2 -d -kfile outputs/RSA/" + STUDENTS[i] + "_decrypted_RSA.txt  -in inputs/" + STUDENTS[i] + "_AES_RW.enc -out outputs/RSA/" + STUDENTS[i] + "_RSA.png -p")
