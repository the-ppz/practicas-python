peso = float(input("Dame tu peso en KG: "))
estatura = float(input("Dame tu estatura en metros: "))

imc = (peso / (estatura)**2)

imc = round(imc,2) # redondeo 

print("Tu IMC es: " + str(imc))