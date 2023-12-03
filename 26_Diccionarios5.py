dias =  ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabados", "Domingos"]
temp = [30.5, 32.6, 31.8, 33.4, 29.8, 30.2, 29.9]

dic_temperaturas = {dias:temp for (dias,temp) in zip(dias, temp)}
print(dic_temperaturas)