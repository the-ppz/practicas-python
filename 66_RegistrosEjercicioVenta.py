# Ejercicio #01

registros = []
bandera = True

while bandera == True:
    print("\n#######################################")
    print("1 - Ingresar un Articulo")
    print("2 - Consultar un Articulo")
    print("3 - Comprar")
    print("4 - Vender")
    print("5 - Eliminar un Articulo")
    print("6 - Salir")
    print("#######################################")
    opcion = int(input("Seleccione una opcion: "))


    if opcion > 0 and opcion < 7:
        if opcion == 1:
            codigo = int(input("Ingrese el codigo del articulo: "))
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            nombre = input("Ingrese el nombre del articulo: ")

            reg = [codigo, cantidad, precio, nombre]
            registros += [reg]

            print("\n#######################################")
            print("##### REGISTRO EXITOSO #####")
            print("#######################################")

        elif opcion == 2:
            consulta = int(input("Ingrese el codigo del articulo: "))
            p = -1 # bandera

            for i in range(len(registros)):
                if consulta == registros[i][0]:
                    p = i # Registro encontrado
                    break;

            if p < 0:
                print("\n\n#######################################")
                print("##### RESULTADO DE LA BUSQUEDA #####")
                print("##### El articulo no existe #####")
                print("#######################################")
            else:
                print("\n\n#######################################")
                print("\n##### RESULTADO DE LA BUSQUEDA #####")
                print("Se encontro el siguiente articulo: ")
                print(f"Cantidad = {registros[p][1]}")
                print(f"Precio = {registros[p][2]}")
                print(f"Nombre = {registros[p][3]}")
                print("#######################################")

        elif opcion == 3:
            consulta = int(input("Ingrese el codigo del articulo: "))
            p = -1  #

            for i in range(len(registros)):
                if consulta == registros[i][0]:
                    p = i
                    break;

            if p < 0:
                print("\n\n#######################################")
                print("##### RESULTADO DE LA BUSQUEDA #####")
                print("##### El articulo no existe #####")
                print("#######################################")
            else:
                print("\n\n#######################################")
                print("\n##### RESULTADO DE LA BUSQUEDA #####")
                cantidad = int(input("Ingresa la cantidad comprada: "))
                registros[p][1] = registros[p][1] + cantidad
                print("Se agrego la cantidad, con EXITO")
                print("#######################################")

        elif opcion == 4:
            consulta = int(input("Ingrese el codigo del articulo: "))
            p = -1  #

            for i in range(len(registros)):
                if consulta == registros[i][0]:
                    p = i
                    break;

            if p < 0:
                print("\n\n#######################################")
                print("##### RESULTADO DE LA BUSQUEDA #####")
                print("##### El articulo no existe #####")
                print("#######################################")
            else:
                print("\n\n#######################################")
                print("\n##### RESULTADO DE LA BUSQUEDA #####")
                cantidad = int(input("Ingresa la cantidad a vender: "))
                registros[p][1] = registros[p][1] - cantidad
                print("Se vendio la cantidad, con EXITO")
                print("#######################################")

        elif opcion == 5:
            consulta = int(input("Ingrese el codigo del articulo: "))
            p = -1

            for i in range(len(registros)):
                if consulta == registros[i][0]:
                    p = i
                    break;

            if p < 0:
                print("\n\n#######################################")
                print("##### RESULTADO DE LA BUSQUEDA #####")
                print("##### El articulo no existe #####")
                print("#######################################")
            else:
                del registros[p]
                print("\n\n#######################################")
                print("##### ELIMINAR REGISTRO #####")
                print("Se elimino exitosamente")
                print("#######################################")

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