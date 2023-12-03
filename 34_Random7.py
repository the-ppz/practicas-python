import random

lista = []
for x in range(20):
    lista.append(random.randint(0,20))

print(lista)
promedio = sum(lista) / len(lista)
print(f"Promedio de los numeros es: {promedio}")