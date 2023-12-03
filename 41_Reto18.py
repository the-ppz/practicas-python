# Esta en el video lo que toca hacer

edad = int(input("Ingrese su edad: "))

if edad > 0 and edad < 100:
    print("Edad Valida")
    
    if edad >= 1 and edad <= 11:
        print("Eres un ninio")
    elif edad >= 12 and edad <= 14:
        print("Eres un adolescente")
    elif edad >= 15 and edad <= 17:
        print("Eres un joven")
    elif edad >= 18 and edad <= 25:
        print("Eres un joven casi adulto")
    elif edad >= 26 and edad <= 35:
        print("Eres un adulto")
    elif edad >= 36 and edad <= 50:
        print("Eres un senior")
    elif edad >= 51 and edad <= 80:
        print("Eres un adulto mayor")
    else:
        print("Estas en una etapa de gloria")
else:
    print("Edad no valida")