""" Escribir un programa que almacene la cadena de caracteres Pass1234+ en una variable, pregunte al 
usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide 
con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas. """

password = "Pass1234+"

p = input("Ingrese la contrasenia: ")

if p == password:
    print("Bienvenido al Sistema.")
else:
    print("No tienes accesso al sistema")