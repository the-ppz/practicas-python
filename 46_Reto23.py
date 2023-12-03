edad = int(input("Ingrese su edad: "))
cumple = input("Es tu cumpleanios si o no: ")
costo = 200
pago = 0

if edad > 0 and edad <= 100:
    if cumple.lower() != "si" and cumple.lower() != "no":
        print("Tienes que poner SI o NO")
    else:
        if cumple.lower() == "si":
            print("Comes GRATIS por ser tu cumpleanios. FELICIDADES!")
        else:
            if edad > 5 and edad < 100:
                print("No cumples anios y no eres un bebe, por favor paga tu buffet")
            if edad <= 5:
                print("Comes GRATIS. Eres un bebe")
            elif edad >= 6 and edad <= 12:
                pago = costo / 2
                print(f"Pagas {pago}")
            elif edad >= 13 and edad <= 15:
                pago = costo - (costo / 4)
                print(f"Pagas {pago}")
            elif edad > 15 and edad <= 50:
                pago = costo
                print(f"Pagas {pago}")
            else:
                pago = costo / 2
                print(f"Pagas la mitad, por ser un adulto mayor. Pagas {pago}")
else:
    print("EDAD NO VALIDA.")