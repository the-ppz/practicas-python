import io

archivo = open("datos1.txt","w")
frase = "**** BIENVENIDO A MANEJOS DE ARCHIVOS ****\n en Python"
archivo.write(frase)
print("Registro Exitoso")
archivo.close()

archivo = open("datos1.txt","r")
# texto = archivo.read()
texto = archivo.readlines() # Devuelve salto de lineas
archivo.close()
print(texto)
for line in texto:
    print(line)