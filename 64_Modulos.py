# Los modulos se encuentran en Funciones_Globales.py

# Importar las funciones
import Funciones_Globales

print(f"El valor de Pi es {Funciones_Globales.pi}")

# Area de un Circulo
area = int(input("Ingrese el radio: "))
ac = round(Funciones_Globales.areaCirculo(area),2)
print(f"El area del circulo es {ac}")

# Raiz Cuadrada
a = float(input("Ingrese el numero: "))
