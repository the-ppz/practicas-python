# Multiples Argumentos
"""
def personasL(nom, ap, *len):
    print(f"Saludos {nom} {ap} \n")
    print(f"Manejas todos estos lenguajes: ")
    for l in len[:]:
        print(f"{l}")

personas = personasL("Franklin", "Alvarez", "C++", "Python", "JavaScript")
print(personas)
"""

#
"""
def listaP(*noms):
    for count, val in enumerate(noms):
        print(f"Saludos {val} eres el numero {count+1}")

        if val == "Pedro":
            print(f"Felicidades {val} tienes un descuento especial")

ejemplo = listaP("Juan", "Fernando", "Pedro", "Frank")
print(ejemplo)
"""

# ** kwargs
def funcionKey(**nombres):
    for key, val in nombres.items():
        print(f"Los nombres son {key} --> valor {val}\n")

demo = funcionKey(nom="Franklin", ape="Alvarez", lenguajeF = "Python")
print(demo)