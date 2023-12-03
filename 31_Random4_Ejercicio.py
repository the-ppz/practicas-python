import random

regalos = ["Laptop", "Silla", "Mesa", "Xbox", "PC", "Mac", "Mouse", "Teclado", "Pantalla", "Monitor"]

for sorteo in range(5):
    premio = regalos[random.randint(0,9)]
    print(f"Sorteo {sorteo+1}, tu premio es: {premio}")