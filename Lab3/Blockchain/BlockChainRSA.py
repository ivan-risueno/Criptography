import math
import random
from Crypto import Random
from Crypto.Util import number
import hashlib


class rsa_key:
    def __init__(self, bits_modulo=2048, e=2 ** 16 + 1):
        """
        genera una clave RSA (de 2048 bits y exponente p´ublico 2**16+1 por defecto)
        """
        self.publicExponent = e
        self.bitsModulo = bits_modulo
        self.generatePQ()
        self.phiN = (self.primeP - 1) * (self.primeQ - 1)
        self.privateExponent = number.inverse(self.publicExponent, self.phiN)
        self.modulus = self.primeP * self.primeQ
        self.privateExponentModulusPhiP = number.inverse(self.publicExponent, self.primeP)
        self.privateExponentModulusPhiQ = number.inverse(self.publicExponent, self.primeQ)
        self.inverseQModulusP = number.inverse(self.primeQ, self.primeP)

    def generatePQ(self):
        found = False
        P = 0
        Q = 0
        while not found:
            P = number.getPrime(int(self.bitsModulo / 2), randfunc=Random.get_random_bytes)
            Q = number.getPrime(int(self.bitsModulo / 2), randfunc=Random.get_random_bytes)
            found = self.checkIfPQAreCorrect(P, Q)

        self.primeP = P
        self.primeQ = Q

    def checkIfPQAreCorrect(self, P, Q):
        phiN = (P - 1) * (Q - 1)
        return math.gcd(self.publicExponent, phiN) == 1 and P != Q

    def sign(self, message):
        """
        Salida: un entero que es la firma de "message" hecha con la clave RSA usando el TCR
        """
        dp = self.privateExponent % (self.primeP - 1)
        dq = self.privateExponent % (self.primeQ - 1)

        pq = number.inverse(self.primeP, self.primeQ)
        qp = number.inverse(self.primeQ, self.primeP)

        c1 = pow(message, dp, self.primeP)
        c2 = pow(message, dq, self.primeQ)

        return (c1 * qp * self.primeQ + c2 * pq * self.primeP) % self.modulus

    def sign_slow(self, message):
        """
        Salida: un entero que es la firma de "message" hecha con la clave RSA sin usar el TCR
        """
        return pow(message, self.privateExponent % ((self.primeP - 1) * (self.primeQ - 1)), self.modulus)


class rsa_public_key:
    def __init__(self, rsa_key):
        """
        genera la clave p´ublica RSA asociada a la clave RSA "rsa_key"
        """
        self.publicExponent = rsa_key.publicExponent
        self.modulus = rsa_key.modulus

    def verify(self, message, signature):
        """
        Salida: el booleano True si "signature" se corresponde con la
        firma de "message" hecha con la clave RSA asociada a la clave
        p´ublica RSA;
        el booleano False en cualquier otro caso.
        """
        return pow(signature, self.publicExponent, self.modulus) == message


class transaction:
    def __init__(self, message, RSAkey):
        """
        genera una transaccion firmando "message" con la clave "RSAkey"
        """
        self.public_key = rsa_public_key(RSAkey)
        self.message = message
        self.signature = RSAkey.sign(message)

    def verify(self):
        """
        Salida: el booleano True si "signature" se corresponde con la
        firma de "message" hecha con la clave RSA asociada a la clave
        p´ublica RSA;
        el booleano False en cualquier otro caso.
        """
        return self.public_key.verify(self.message, self.signature)


class block:
    def __init__(self):
        """
        crea un bloque (no necesariamente v´alido)
        """
        self.block_hash = 0
        self.previous_block_hash = 0
        self.transaction = 0
        self.seed = 0

    def generate_hash(self, correct_hash=True):
        # Por defecto es conveniente llamar a esta función sin ningún parámetro
        while True:
            seed = random.randint(0, 2 ** 256)
            entrada = str(self.previous_block_hash)
            entrada = entrada + str(self.transaction.public_key.publicExponent)
            entrada = entrada + str(self.transaction.public_key.modulus)
            entrada = entrada + str(self.transaction.message)
            entrada = entrada + str(self.transaction.signature)
            entrada = entrada + str(seed)
            h = int(hashlib.sha256(entrada.encode()).hexdigest(), 16)
            if not correct_hash or h < pow(2, 256 - 16):  # Por defecto se busca un hash válido
                self.block_hash = h
                self.seed = seed
                break

    def genesis(self, transaction):
        """
        genera el primer bloque de una cadena con la transacci´on "transaction"
        que se caracteriza por:
        - previous_block_hash=0
        - ser v´alido
        """
        self.previous_block_hash = 0
        self.transaction = transaction
        self.generate_hash()  # Generamos un hash válido

    def next_block(self, transaction):
        """
        genera un bloque v´alido seguiente al actual con la transacci´on "transaction"
        """
        b = block()
        b.transaction = transaction
        b.previous_block_hash = self.block_hash
        b.generate_hash()  # Generamos un hash válido
        return b

    def verify_block(self):
        """
        Verifica si un bloque es v´alido:
        -Comprueba que el hash del bloque anterior cumple las condiciones exigidas
        -Comprueba que la transacci´on del bloque es v´alida
        -Comprueba que el hash del bloque cumple las condiciones exigidas
        Salida: el booleano True si todas las comprobaciones son correctas;
        el booleano False en cualquier otro caso.
        """
        a = self.transaction.verify()
        b = self.block_hash < pow(2, 256 - 16)
        c = self.previous_block_hash < pow(2, 256 - 16)
        return a and b and c


class block_chain:
    def __init__(self, transaction):
        """
        genera una cadena de bloques que es una lista de bloques,
        el primer bloque es un bloque "genesis" generado amb la transacci´o "transaction"
        """
        self.list_of_blocks = []
        b = block()
        b.genesis(transaction)
        self.list_of_blocks.append(b)

    def add_block(self, transaction):
        """
        a~nade a la cadena un nuevo bloque v´alido generado con la transacci´on "transaction"
        """
        b = self.list_of_blocks[-1].next_block(transaction)
        self.list_of_blocks.append(b)

    def verify(self):
        """
        verifica si la cadena de bloques es v´alida:
        - Comprueba que todos los bloques son v´alidos
        - Comprueba que el primer bloque es un bloque "genesis"
        - Comprueba que para cada bloque de la cadena el siguiente es correcto
        Salida: el booleano True si todas las comprobaciones son correctas;
        en cualquier otro caso, el booleano False y un entero
        correspondiente al ´ultimo bloque v´alido
        """
        for b in self.list_of_blocks:
            # No hace falta verificar que el primero es génesis, ya que esto es invariante entre todas las instancias
            # de block_chain
            if not b.verify_block():
                return False

        return True
