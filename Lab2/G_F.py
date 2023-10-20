class G_F:

    #Genera un cuerpo finito usando como polinomio irreducible el dado
    #representado como un entero. Por defecto toma el polinomio del AES.
    #Los elementos del cuerpo los representaremos por enteros 0<= n <= 255.

    def __init__(self, Polinomio_Irreducible = 0x11B):

        #Entrada: un entero que representa el polinomio para construir el cuerpo
        #Tabla_EXP y Tabla_LOG dos tablas, la primera tal que en la posici ́on
        #i- ́esima tenga valor a=g**i y la segunda tal que en la posici ́on a- ́esima
        #tenga el valor i tal que a=g**i. (g generador del cuerpo finito
        #representado por el menor entero entre 0 y 255.)

        generador = self.encontrarGenerador()

        self.Polinomio_Irreducible = Polinomio_Irreducible
        self.Tabla_EXP, self.Tabla_LOG = self.generarTablas(generador)

    def encontrarGenerador(self):
        for generador in range(2, 256):
            es_generador = True
            elemento = 1
            for _ in range(8):
                elemento = (elemento * generador) % 256
                if elemento == 1:
                    es_generador = False
                    break
            if es_generador:
                return generador

        return None

    def productoLento(self, a, b):
        c = 0
        for _ in range(8):
            if b & 1:
                c ^= a

            bit_mas_alto = a & 128
            a <<= 1
            if bit_mas_alto:
                a ^= self.Polinomio_Irreducible

            b >>= 1
        return c

    def generarTablas(self, generador):
        EXP = {}
        LOG = {}
        while generador < 255:
            elemento = 1
            bucle = False
            for i in range(255):
                EXP[i] = elemento
                LOG[elemento] = i
                elemento = self.productoLento(elemento, generador)
                if elemento == 1 and i < 254:
                    bucle = True
                    break
            if not bucle:
                break
            generador += 1
        return EXP, LOG

    def xTimes(self, n):

        #Entrada: un elemento del cuerpo representado por un entero entre 0 y 255
        #Salida: un elemento del cuerpo representado por un entero entre 0 y 255
        #que es el producto en el cuerpo de ’n’ y 0x02 (el polinomio X).

        if n & 0x80:
            return ((n << 1) ^ 0x1B) & 0xFF
        else:
            return (n << 1) & 0xFF

    def producto(self, a, b):

        #Entrada: dos elementos del cuerpo representados por enteros entre 0 y 255
        #Salida: un elemento del cuerpo representado por un entero entre 0 y 255
        #que es el producto en el cuerpo de la entrada.
        #Atenci ́on: Se valorar ́a la eficiencia. No es lo mismo calcularlo
        #usando la definici ́on en t ́erminos de polinomios o calcular
        #usando las tablas Tabla_EXP y Tabla_LOG.

        return self.Tabla_EXP[(self.Tabla_LOG[a] + self.Tabla_LOG[b]) % 255]

    def inverso(self, n):

        #Entrada: un elementos del cuerpo representado por un entero entre 0 y 255
        #Salida: 0 si la entrada es 0,
        #el inverso multiplicativo de n representado por un entero entre
        #1 y 255 si n <> 0.
        #Atenci ón: Se valorar ́a la eficiencia.

        if n == 0:
            return 0

        return self.Tabla_EXP[255 - self.Tabla_LOG[n]]

a = G_F()

print(a.productoLento(12,240))
print(a.producto(12, 240))
print(a.inverso(11))