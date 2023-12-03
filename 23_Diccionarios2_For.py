prueba_deportiva = {"Jorge": 500, 'Diana': 600, 'Rodrigo': 800, 'Julia': 750, 'Li': 900, "lista":[1,2,3]}
nota = prueba_deportiva
print(nota)
print(nota["Rodrigo"])
print(nota["lista"][0])

v1, v2, v3, v4, v5, v6 = nota
print(v1)
print(v2)
print(v3)
print(v4)
print(v5)
print(v6)

print("*****FOR********")
for d in nota:
    print(d)