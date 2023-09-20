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

        self.Polinomio_Irreducible = Polinomio_Irreducible
        self.Tabla_EXP = generarTablaEXP()
        self.Tabla_LOG = generarTablaLOG()
    
    def generarTablaEXP():
        return

    def generarTablaLOG():
        return

    def xTimes(self, n):

        #Entrada: un elemento del cuerpo representado por un entero entre 0 y 255
        #Salida: un elemento del cuerpo representado por un entero entre 0 y 255
        #que es el producto en el cuerpo de ’n’ y 0x02 (el polinomio X).
        return

    def producto(self, a, b):

        #Entrada: dos elementos del cuerpo representados por enteros entre 0 y 255
        #Salida: un elemento del cuerpo representado por un entero entre 0 y 255
        #que es el producto en el cuerpo de la entrada.
        #Atenci ́on: Se valorar ́a la eficiencia. No es lo mismo calcularlo
        #usando la definici ́on en t ́erminos de polinomios o calcular
        #usando las tablas Tabla_EXP y Tabla_LOG.
        return

    def inverso(self, n):

        #Entrada: un elementos del cuerpo representado por un entero entre 0 y 255
        #Salida: 0 si la entrada es 0,
        #el inverso multiplicativo de n representado por un entero entre
        #1 y 255 si n <> 0.
        #Atenci ón: Se valorar ́a la eficiencia.
        return