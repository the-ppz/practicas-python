import random 

personas = ["Alex", "Bob", "Carol", "Dave", "Flow", "Katie", "Nate"]

dic_descuentos = {per:random.randint(1,100) for per in personas}
print(dic_descuentos)