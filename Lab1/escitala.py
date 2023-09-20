archivo = open ("KH-j76GH", "r")
txt = archivo.read()
sz = len(txt)
print(sz) #imprime el numero de caracteres del texto
#ahora sz es 378178, los divisores son 1, 2, 173, 346, 1093, 2186, 189089, 378178

#s sera uno de esos numeros
#hay que mirar las posiciones [0, s, s*2, s*3, etc]

#el 173 es para estos caracteres, no para todos los casos
s = 173
mensaje = ""
i = 0

while i < sz:
    mensaje += txt[i]
    i += s

print(mensaje)
