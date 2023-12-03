import random 

personas = ["Alex", "Bob", "Carol", "Dave", "Flow", "Katie", "Nate"]

dic_descuentos = {per:random.randint(1,100) for per in personas}
print(dic_descuentos)
print("################### Descuento Mayores a 50 #########################")

salida = {personas:dic_descuentos for (personas, dic_descuentos) in dic_descuentos.items() if dic_descuentos > 50}
print(salida)