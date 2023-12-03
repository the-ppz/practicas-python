import random

val = random.randint(1,20)
print(val)

val2 = random.randrange(1,20,8) # Con incrementos
print(val2)

decimal = random.random()
print(decimal)
decimal2 = round(random.random(),2)
print(decimal2)

decimal3 = random.uniform(1,10) # Rango de donde a donde
print(decimal3)
decimal4 = round(random.uniform(1,10),2)
print(decimal4)