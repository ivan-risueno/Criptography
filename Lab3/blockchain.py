class rsa_key:
    def __init__(self,bits_modulo=2048,e=2**16+1):
        '''
        genera una clave RSA (de 2048 bits y exponente p´ublico 2**16+1 por defecto)
        '''
        self.publicExponent
        self.privateExponent
        self.modulus
        self.primeP
        self.primeQ
        self.privateExponentModulusPhiP
        self.privateExponentModulusPhiQ
        self.inverseQModulusP

    def sign(self,message):
        '''
        Salida: un entero que es la firma de "message" hecha con la clave RSA usando el TCR
        '''

    def sign_slow(self,message):
        '''
        Salida: un entero que es la firma de "message" hecha con la clave RSA sin usar el TCR
        '''

class rsa_public_key:
    def __init__(self, rsa_key):
        '''
        genera la clave p´ublica RSA asociada a la clave RSA "rsa_key"
        '''
        self.publicExponent
        self.modulus

    def verify(self, message, signature):
        '''
        Salida: el booleano True si "signature" se corresponde con la
        firma de "message" hecha con la clave RSA asociada a la clave
        p´ublica RSA;
        el booleano False en cualquier otro caso.
        '''

class transaction:
    def __init__(self, message, RSAkey):
        '''
        genera una transaccion firmando "message" con la clave "RSAkey"
        '''
        self.public_key
        self.message
        self.signature

    def verify(self):
        '''
        Salida: el booleano True si "signature" se corresponde con la
        firma de "message" hecha con la clave RSA asociada a la clave
        p´ublica RSA;
        el booleano False en cualquier otro caso.
        '''

class block:
    def __init__(self):
        '''
        crea un bloque (no necesariamente v´alido)
        '''
        self.block_hash
        self.previous_block_hash
        self.transaction
        self.seed

    def genesis(self,transaction):
        '''
        genera el primer bloque de una cadena con la transacci´on "transaction"
        que se caracteriza por:
        - previous_block_hash=0
        - ser v´alido
        '''

    def next_block(self, transaction):
        '''
        genera un bloque v´alido seguiente al actual con la transacci´on "transaction"
        '''

    def verify_block(self):
        '''
        Verifica si un bloque es v´alido:
        -Comprueba que el hash del bloque anterior cumple las condiciones exigidas
        -Comprueba que la transacci´on del bloque es v´alida
        -Comprueba que el hash del bloque cumple las condiciones exigidas
        Salida: el booleano True si todas las comprobaciones son correctas;
        el booleano False en cualquier otro caso.
        '''

class block_chain:
    def __init__(self,transaction):
        '''
        genera una cadena de bloques que es una lista de bloques,
        el primer bloque es un bloque "genesis" generado amb la transacci´o "transaction"
        '''
        self.list_of_blocks

    def add_block(self,transaction):
        '''
        a~nade a la cadena un nuevo bloque v´alido generado con la transacci´on "transaction"
        '''

    def verify(self):
        '''
        verifica si la cadena de bloques es v´alida:
        - Comprueba que todos los bloques son v´alidos
        - Comprueba que el primer bloque es un bloque "genesis"
        - Comprueba que para cada bloque de la cadena el siguiente es correcto
        Salida: el booleano True si todas las comprobaciones son correctas;
        en cualquier otro caso, el booleano False y un entero
        correspondiente al ´ultimo bloque v´alido
        '''