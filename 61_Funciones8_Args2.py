# Suma con *args

def sumar(*num):
    return sum(num)

ejemplo1 = sumar(23,45,23)
print(f"La suma es {ejemplo1}\n\n")


# Mayor de dos numeros con args
def numMayor(*num):
    return max(num)

ejemplo2 = numMayor(34,233,3,432)
print(f"El numero mayor es {ejemplo2}\n\n")


# Crear una funcion que sume N argumentos sin la funcion sum
def suma(*num):
    suma = 0
    for n in num[:]: # Muestra todos los numeros
        suma += n
    return suma

n = suma(3,4,5,6)
print(f"{n}\n\n")

# El mayor de dos numeros sin la funcion max
def mayor(*num):
    m = num[0]
    for n in num[1:]:
        if n > m:
            m = n
    return m

ejemplo3 = mayor(3,4,5,6)
print(ejemplo3)