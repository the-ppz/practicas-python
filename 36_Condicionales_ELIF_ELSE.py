# IF - ELIF - ELSE

a = 10
b = 10

if a > b:
    print("A es mayor")
    print(str(a) + " > " + str (b))
    
elif a < b:
    print("B es mayor")
    print(str(b) + " > " + str (a))
    
elif a == b:
    print("A y B son iguales")
    print(str(a) + " = " + str (b))   
     
else:
    print("A y B son diferentes")
    print(str(a) + " != " + str (b))