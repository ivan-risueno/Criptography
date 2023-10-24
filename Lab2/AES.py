from Lab2.G_F import G_F


class AES:
    """
    Documento de referencia:
    Federal Information Processing Standards Publication (FIPS) 197: Advanced Encryption
    Standard (AES) https://doi.org/10.6028/NIST.FIPS.197-upd1
    El nombre de los m´etodos, tablas, etc son los mismos (salvo capitalizaci´on)
    que los empleados en el FIPS 197
    """

    def initRcon(self):
        rcon = [[0 for _ in range(4)] for _ in range(10)]
        rcon[0][0] = 0x01
        for i in range(1, 10):
            rcon[i][0] = self.gf.xTimes(rcon[i - 1][0])

        return rcon

    def __init__(self, key, Polinomio_Irreducible=0x11B):
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
        rounds_by_key_size = {16: 10, 24: 12, 32: 14}
        self.Polinomio_Irreducible = Polinomio_Irreducible
        self.gf = G_F()
        self.Nr = rounds_by_key_size[len(key)]
        self.Nk = len(key) / 4
        self.SBox = (
            0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
            0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
            0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
            0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
            0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
            0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
            0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
            0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
            0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
            0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
            0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
            0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
            0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
            0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
            0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
            0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
        )
        self.InvSBox = (
            0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
            0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
            0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
            0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
            0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
            0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
            0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
            0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
            0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
            0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
            0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
            0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
            0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
            0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
            0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
            0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D
        )
        self.Rcon = self.initRcon()
        # self.InvMixMatrix

    def SubBytes(self, State):
        """miguel
        5.1.1 SUBBYTES()
        FIPS 197: Advanced Encryption Standard (AES)
        """
        for i in range(len(State)):
            State[i] = self.SBox[State[i]]

    def InvSubBytes(self, State):
        """miguel
        5.3.2 INVSUBBYTES()
        FIPS 197: Advanced Encryption Standard (AES)
        """
        for i in range(len(State)):
            State[i] = self.InvSBox[State[i]]

    def ShiftRows(self, State):
        """ivan
        5.1.2 SHIFTROWS()
        FIPS 197: Advanced Encryption Standard (AES)
        """

        ret = State

        for i in range(1, len(State)):
            for n in range(0, i):
                tmp = ret[i][0]
                for j in range(len(State[i]) - 1):
                    ret[i][j] = State[i][(j + 1) % 4]
                ret[i][len(State[i]) - 1] = tmp
        return ret

    def InvShiftRows(self, State):
        """ivan
        5.3.1 INVSHIFTROWS()
        FIPS 197: Advanced Encryption Standard (AES)
        """
        ret = State

        for i in range(1, len(State)):
            for n in range(0, i):
                tmp = ret[i][len(State[i]) - 1]
                for j in range(len(State[i]) - 1, 0, -1):
                    ret[i][j] = State[i][(j - 1) % 4]
                ret[i][0] = tmp
        return ret

    def GaloisMulti(x, y):
        p = 0
        for c in range(8):
            if b & 1:
                p ^= a
            a <<= 1
            if a & 0x100:
                a ^= 0x11b
            b >>= 1
        return p

    def MixColumns(self, State):
        """miguel
        5.1.3 MIXCOLUMNS()
        FIPS 197: Advanced Encryption Standard (AES)
        """
        nState = []
        for i in range(4):
            col = self.state[c * 4:(c + 1) * 4]
            nState.extend((
                AES.GaloisMulti[0x02][col[0]] ^ AES.GaloisMulti[0x03][col[1]] ^ col[2] ^ col[3],
                col[0] ^ AES.GaloisMulti[0x02][col[1]] ^ AES.GaloisMulti[0x03][col[2]] ^ col[3],
                col[0] ^ col[1] ^ AES.GaloisMulti[0x02][col[2]] ^ AES.GaloisMulti[0x03][col[3]],
                AES.GaloisMulti[0x03][col[0]] ^ col[1] ^ col[2] ^ AES.GaloisMulti[0x02][col[3]],
            ))
        self.State = nState

    def InvMixColumns(self, State):
        """miguel
        5.3.3 INVMIXCOLUMNS()
        FIPS 197: Advanced Encryption Standard (AES)
        """
        nState = []
        for i in range(4):
            col = self.state[c * 4:(c + 1) * 4]
            nState.extend((
                AES.GaloisMulti[0x0E][col[0]] ^ AES.GaloisMulti[0x0B][col[1]] ^ AES.GaloisMulti[0x0D][col[2]] ^
                AES.GaloisMulti[0x09][col[3]],
                AES.GaloisMulti[0x09][col[0]] ^ AES.GaloisMulti[0x0E][col[1]] ^ AES.GaloisMulti[0x0B][col[2]] ^
                AES.GaloisMulti[0x0D][col[3]],
                AES.GaloisMulti[0x0D][col[0]] ^ AES.GaloisMulti[0x09][col[1]] ^ AES.GaloisMulti[0x0E][col[2]] ^
                AES.GaloisMulti[0x0B][col[3]],
                AES.GaloisMulti[0x0B][col[0]] ^ AES.GaloisMulti[0x0D][col[1]] ^ AES.GaloisMulti[0x09][col[2]] ^
                AES.GaloisMulti[0x0E][col[3]],
            ))
        self.State = nState

    def AddRoundKey(self, State, roundKey):
        """ivan
        5.1.4 ADDROUNDKEY()
        FIPS 197: Advanced Encryption Standard (AES)
        """
        ret = State
        for i in range(0, len(State)):
            for j in range(0, len(State[i])):
                ret[i][j] = State[i][j] ^ roundKey[j][i]
        return ret

    def rotWord(self, word):
        assert len(word) == 4
        w = [0, 0, 0, 0]
        w[0] = word[1]
        w[1] = word[2]
        w[2] = word[3]
        w[3] = word[0]
        return w

    def subWord(self, w):
        assert len(w) == 4
        return [self.SBox[w[0]], self.SBox[w[1]], self.SBox[w[2]], self.SBox[w[3]]]

    def KeyExpansion(self, key):
        """ivan
        5.2 KEYEXPANSION()
        FIPS 197: Advanced Encryption Standard (AES)
        """

        # key es un array con los valores de la llave, del estilo [0x12, 0x34, 0x56, 0x78, 0x90]
        w = [[0 for _ in range(4)] for _ in range(4 * (self.Nr + 1))]
        i = 0
        while i <= self.Nk - 1:
            w[i] = [key[4 * i], key[4 * i + 1], key[4 * i + 2], key[4 * i + 3]]
            i += 1

        while i <= 4 * self.Nr + 3:
            temp = w[i - 1]

            if i % self.Nk == 0:
                temp = self.subWord(self.rotWord(temp))
                temp[0] ^= self.Rcon[int(i / self.Nk) - 1][0]  # Todos los bytes de RCON son 0 menos el primero
            elif self.Nk > 6 and i % self.Nk == 4:
                temp = self.subWord(temp)

            w[i] = [b ^ c for b, c in zip(w[int(i - self.Nk)], temp)]
            i += 1

        return w

    def Cipher(self, State, Nr, Expanded_KEY):
        """ivan
        5.1 Cipher(), Algorithm 1 p´ag. 12
        FIPS 197: Advanced Encryption Standard (AES)
        """
        State = self.AddRoundKey(State, Expanded_KEY[0:4])
        for round in range(1, Nr - 1):
            State = self.SubBytes(State)
            State = self.ShiftRows(State)
            State = self.MixColumns(State)
            State = self.AddRoundKey(State, Expanded_KEY[4 * round:4 * round + 4])

        State = self.SubBytes(State)
        State = self.ShiftRows(State)
        State = self.AddRoundKey(State, Expanded_KEY[4 * Nr:4 * Nr + 4])
        return State

    def InvCipher(self, State, Nr, Expanded_KEY):
        """ivan
        5. InvCipher()
        Algorithm 3 p´ag. 20 o Algorithm 4 p´ag. 25. Son equivalentes
        FIPS 197: Advanced Encryption Standard (AES)
        """
        State = self.AddRoundKey(State, Expanded_KEY[4*Nr:4*Nr+4])
        for round in range(Nr - 1, 1, -1):
            State = self.InvShiftRows(State)
            State = self.InvSubBytes(State)
            State = self.AddRoundKey(State, Expanded_KEY[4*round:4*round+4])
            State = self.InvMixColumns(State)

        State = self.InvShiftRows(State)
        State = self.InvSubBytes(State)
        State = self.AddRoundKey(State, Expanded_KEY[0:4])
        return State

    def printState(self, State, functionCalled):
        print(functionCalled)
        for i in range(len(State)):
            print(hex(State[i][0]) + " " + hex(State[i][1]) + " " + hex(State[i][2]) + " " + hex(State[i][3]))
        print()

    def encrypt_file(self, fichero):
        """miguel
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
        """miguel
        Entrada: Nombre del fichero a descifrar
        Salida: Fichero descifrado usando la clave utilizada en el constructor
        de la clase.
        Para descifrar se usar´a el modo CBC, con el IV guardado en los 16
        primeros bytes del fichero cifrado, y se eliminar´a el padding
        PKCS7 a~nadido al cifrar el fichero.
        El nombre de fichero descifrado ser´a el obtenido al a~nadir el sufijo .dec
        al nombre del fichero a descifrar: NombreFichero --> NombreFichero.dec
        """


k = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
a = AES(k)
key = a.KeyExpansion(k)
input = [[0x32, 0x88, 0x31, 0xe0],
         [0x43, 0x5a, 0x31, 0x37],
         [0xf6, 0x30, 0x98, 0x07],
         [0xa8, 0x8d, 0xa2, 0x34]]
ret = a.AddRoundKey(input, key[0:4])
a.printState(ret, "AddRoundKey")
ret = [[0xd4, 0xe0, 0xb8, 0x1e],
       [0x27, 0xbf, 0xb4, 0x41],
       [0x11, 0x98, 0x5d, 0x52],
       [0xae, 0xf1, 0xe5, 0x30]]
a.printState(ret, "SubBytes")
ret = a.ShiftRows(ret)
a.printState(ret, "ShiftRows")
ret = [[0x4, 0xe0, 0x48, 0x28],
       [0x66, 0xcb, 0xf8, 0x6],
       [0x81, 0x19, 0xd3, 0x26],
       [0xe5, 0x9a, 0x7a, 0x4c]]
a.printState(ret, "MixColumn")
ret = a.AddRoundKey(ret, key[4 * 1:4 * 1 + 4])
a.printState(ret, "AddRoundKey")
