import math
from itertools import combinations
from sympy import *

#usar itertools para buscar los trigramas del ingles, con permutations(lista, 3), la lista es una lista de posibles permutaciones de trigramas en la lista

#inicio
archivo = open ("descarga", "r")
txt = archivo.read()
sz = len(txt) #la longitud total
print(sz)
trisz = sz // 3 #los trigramas
print (trisz)

#calcular frecuencia
#voy a hacerlo con diccionarios que el metodo de Hao es muy raro

i = 0
freqs = { }
while i < trisz:
    j = i*3
    trip = txt[j:j+3]
    if freqs.get(trip) is None:
        freqs[trip] = 1
    else:
        freqs[trip] += 1
    i += 1

#print(freqs)

#maximos de frecuencia

freqs = dict(sorted(freqs.items(), key=lambda item: item[1]))

max = list(freqs)[-1]
fmax = freqs[max]
print(max + ' ' + str(fmax))

max2 = list(freqs)[-2]
fmax2 = freqs[max2]
print(max2 + ' ' + str(fmax2))

max3 = list(freqs)[-3]
fmax3 = freqs[max3]
print(max3 + ' ' + str(fmax3))

#descifrar

letras = {}
for i in range(0,26):
    letras[chr(i+65)] = i

M = Matrix([[letras[max[0]],letras[max[1]],letras[max[2]]],
 [letras[max2[0]],letras[max2[1]],letras[max2[2]]],
 [letras[max3[0]],letras[max3[1]],letras[max3[2]]]])
print(M)

tring = ["THE","AND","THA","ENT","ING"]
comb = combinations([0,1,2,3,4],3)

for i in list(comb):
    ti1 = tring[i[0]]
    ti2 = tring[i[1]]
    ti3 = tring[i[2]]
    A = Matrix([[letras[ti1[0]],letras[ti1[1]],letras[ti1[2]]],
     [letras[ti2[0]],letras[ti2[1]],letras[ti2[2]]],
     [letras[ti3[0]],letras[ti3[1]],letras[ti3[2]]]])

    if gcd(26,A.det()) == 1:
         print(i)
         #inversa mod 26
         B = A.inv_mod(26)
         # A-1 * M
         Ht = B * M
         # RES T
         H = Ht.transpose()
         D = H.inv_mod(26)
         # Desxifrar text i escriure.
         res = ""
         for j in range(0,25):
            k = j*3
            aux = Matrix([[letras[txt[k]]],[letras[txt[k+1]]],[letras[txt[k+2]]]])
            aux2 = D * aux
            aux2 = aux2.applyfunc(lambda x : x % 26)
            res += chr(aux2[0]+65)
            res += chr(aux2[1]+65)
            res += chr(aux2[2]+65)
         print(res)