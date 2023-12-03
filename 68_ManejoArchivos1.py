import io

archivo = open("datos.txt","w")
texto = "**** LENGUAJES DE PROGRAMACION ****\n"
archivo.write(texto)
texto = "PHP\n"
archivo.write(texto)
texto = "Python\n"
archivo.write(texto)
texto = "Java\n"
archivo.write(texto)
texto = "C++\n"
archivo.write(texto)

archivo.close()