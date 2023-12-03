# Unir dos lista con el metodo zip
pais = ["China", "India", "Estados Unidos", "Indonesia"]
poblacion = [1391, 1364, 327, 264]

lista_poblacion = list(zip(pais,poblacion))
print(lista_poblacion)

for pa, po in zip(pais,poblacion):
    print(f"En {pa} hay {po} millones de Estudiantes")