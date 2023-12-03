nombre = "Rodrigo"
nombre2 = "rodrigo"

if nombre == nombre2:
    print("Son iguales")
else:
    print("Son diferentes")
    
if nombre == "Rodrigo" or nombre2 == "rodrigo":
    print("Son iguales")
else:
    print("Son diferentes")
   
a = "Y"
    
if a in ["y", "Y", "YES", "yes"]:
    print("Si existe el elemento en la lista")
else:
    print("No existe el elemento en la lista")