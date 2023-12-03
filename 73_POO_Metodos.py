# Sobre carga de metodos
# Herencia
"""
class Persona:
    def __init__(self, especialidad):
        self.especialidad = especialidad
        self.celular = 123456

    def mensaje(self):
        print("Mensaje de la clase Persona")

    def NivelEspecialidad(self):
        print(f"Nivel de especialidad {self.especialidad}")

class Obrero(Persona):
    def __init__(self,especialidad):
        super().__init__(especialidad)

    def mensaje(self):
        print("Mensaje de la clase Obrero")

    def NivelEspecialidad(self):
        print(f"Nivel de especialidad Obrero {self.especialidad}")


class Ingeniero(Persona):
    def __init__(self, especialidad):
        super().__init__(especialidad)

    def mensaje(self):
        print("Mensaje de la clase Ingeniero")

p1 = Persona(3)
p1.mensaje()
p1.NivelEspecialidad()

p2 = Obrero(7)
p2.mensaje()
p2.NivelEspecialidad()
"""

# Metodos Magicos
# str
class Tiempo:
    def __init__(self,h=0,m=0,s=0):
        self.hora = h
        self.minutos = m
        self.segundos = s

    # Metodo magico
    def __str__(self):
        return f"Tiempo {self.hora} {self.minutos} {self.segundos}"

    #
    def imprimir(self):
      return f"Tiempo {self.hora} {self.minutos} {self.segundos}"

ejemplo = Tiempo(12,25,30)
print(ejemplo.imprimir())
print(ejemplo) # Metodo magico

print("\n\n\n")

# __add -> se usa para sumas
# __sub -> se usa para restas
class Time:
    def __init__(self, h=0, m=0, s=0):
        self.hora = h
        self.minutos = m
        self.segundos = s

    def __add__(self, other):
        h = self.hora + other.hora
        m = self.minutos + other.minutos
        s = self.segundos + other.segundos
        print(f"Suma de horas {h, m, s}")

    def __sub__(self, other):
        h = self.hora - other.hora
        m = self.minutos - other.minutos
        s = self.segundos - other.segundos
        print(f"Resta de horas {h, m, s}")

a = Time(2,16,48)
b = Time(3,51,22)
print(a+b)
print(a-b)