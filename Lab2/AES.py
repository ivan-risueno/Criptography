class AES:
    """
    Documento de referencia:
    Federal Information Processing Standards Publication (FIPS) 197: Advanced Encryption
    Standard (AES) https://doi.org/10.6028/NIST.FIPS.197-upd1
    El nombre de los m´etodos, tablas, etc son los mismos (salvo capitalizaci´on)
    que los empleados en el FIPS 197
    """
    def __init__(self, key, Polinomio_Irreducible = 0x11B):
        """
        Entrada:
        key: bytearray de 16 24 o 32 bytes
        Polinomio_Irreducible: Entero que representa el polinomio para construir
        el cuerpo
        SBox: equivalente a la tabla 4, p´ag. 14
        InvSBOX: equivalente a la tabla 6, p´ag. 23
        Rcon: equivalente a la tabla 5, p´ag. 17
        InvMixMatrix : equivalente a la matriz usada en 5.3.3, p´ag. 24
        """
        self.Polinomio_Irreducible = Polinomio_Irreducible
        self.SBox
        self.InvSBox
        self.Rcon
        self.InvMixMatrix

    def SubBytes(self, State):
        """miguel
        5.1.1 SUBBYTES()
        FIPS 197: Advanced Encryption Standard (AES)
        """

    def InvSubBytes(self, State):
        """miguel
        5.3.2 INVSUBBYTES()
        FIPS 197: Advanced Encryption Standard (AES)
        """

    def ShiftRows(self, State):
        """ivan
        5.1.2 SHIFTROWS()
        FIPS 197: Advanced Encryption Standard (AES)
        """

    def InvShiftRows(self, State):
        """ivan
        5.3.1 INVSHIFTROWS()
        FIPS 197: Advanced Encryption Standard (AES)
        """

    def MixColumns(self, State):
        """miguel
        5.1.3 MIXCOLUMNS()
        FIPS 197: Advanced Encryption Standard (AES)
        """

    def InvMixColumns(self, State):
        """miguel
        5.3.3 INVMIXCOLUMNS()
        FIPS 197: Advanced Encryption Standard (AES)
        """

    def AddRoundKey(self, State, roundKey):
        """ivan
        5.1.4 ADDROUNDKEY()
        FIPS 197: Advanced Encryption Standard (AES)
        """

    def KeyExpansion(self, key):
        """ivan
        5.2 KEYEXPANSION()
        FIPS 197: Advanced Encryption Standard (AES)
        """
    def Cipher(self, State, Nr, Expanded_KEY):
        """miguel
        5.1 Cipher(), Algorithm 1 p´ag. 12
        FIPS 197: Advanced Encryption Standard (AES)
        """

    def InvCipher(self, State, Nr, Expanded_KEY):
        """miguel
        5. InvCipher()
        Algorithm 3 p´ag. 20 o Algorithm 4 p´ag. 25. Son equivalentes
        FIPS 197: Advanced Encryption Standard (AES)
        """

    def encrypt_file(self, fichero):
        """ivan
        Entrada: Nombre del fichero a cifrar
        Salida: Fichero cifrado usando la clave utilizada en el constructor
        de la clase.
        Para cifrar se usar´a el modo CBC, con IV generado aleatoriamente
        y guardado en los 16 primeros bytes del fichero cifrado.
        El padding usado ser´a PKCS7.
        El nombre de fichero cifrado ser´a el obtenido al a~nadir el sufijo .enc
        al nombre del fichero a cifrar: NombreFichero --> NombreFichero.enc
        """

    def decrypt_file(self, fichero):
        """ivan
        Entrada: Nombre del fichero a descifrar
        Salida: Fichero descifrado usando la clave utilizada en el constructor
        de la clase.
        Para descifrar se usar´a el modo CBC, con el IV guardado en los 16
        primeros bytes del fichero cifrado, y se eliminar´a el padding
        PKCS7 a~nadido al cifrar el fichero.
        El nombre de fichero descifrado ser´a el obtenido al a~nadir el sufijo .dec
        al nombre del fichero a descifrar: NombreFichero --> NombreFichero.dec
        """
