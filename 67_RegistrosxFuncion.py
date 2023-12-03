# Crear las funciones
# Agregar
def agregar(e):
    try:
        mat = int(input("Ingrese la matricula: "))
        if mat not in e:
            e = e + [mat]
            print("Registro Exitoso")
        else:
            print("Ya estas matriculado")
        return e
    except:
        print("No se pudo registrar")

# Eliminar
def eliminar(e):
    try:
        mat = int(input("Ingrese la matricula: "))
        if mat in e:
            e.remove(mat)
            print("Se elimino la matricula")
        else:
            print("No estas mattriculado")
    except:
        print("No existe el registro")

# Consultar
def consultar(e):
    try:
        mat = int(input("Ingrese la matricula: "))
        if mat in e:
            print(f"Si estas matriculado {mat}")
        else:
            print("No estas mattriculado")
    except:
        print("No se pudo consultar")

# Cupo
def cupo(e):
    try:
        num = len(e)
        print(f"Numeros de matriculados {num}")
    except:
        print("No hay matriculados")

e = []
bandera = True

while bandera == True:
    print("\n#######################################")
    print("1 - Agregar Matricula")
    print("2 - Eliminar Matricula")
    print("3 - Consultar Matricula")
    print("4 - Cupo Actual")
    print("5 - Salir")
    print("#######################################")
    opcion = int(input("Seleccione una opcion: "))

    if opcion > 0 and opcion < 6:
        if opcion == 1:
            e = agregar(e)

        elif opcion == 2:
            e = eliminar(e)

        elif opcion == 3:
            consultar(e)

        elif opcion == 4:
            cupo(e)

        else:
            print("\n\n#######################################")
            print("HASTA PRONTO")
            print("#######################################")
            bandera = False

    else:
        print("\n\n#######################################")
        print("######## OPCION NO VALIDA #############")
        print("Seleccione una opcion del 1 al 6")
        print("#######################################")