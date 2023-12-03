import random

lista = [1,2,3,4,5,6,7,8,9]

print(random.sample(lista,2))

for valores in random.sample(lista,5):
    print(f"Los valores son {valores}")