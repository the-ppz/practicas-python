# Funciones *args
print("\n")

def saludo(*personas):
    print(personas)
    print(f"Persona #2 es {personas[1]}")

saludo("Juan","Frank","Luis","Javier")

print("\n\n")

def saludo2(*personas):
    for people in personas:
        print(f"Hola {people}, bienvenido")

saludo2("Juan","Frank","Luis","Javier")