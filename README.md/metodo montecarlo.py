import random
import math

cuantos= 1000
cuantos_si= 0

for i in range(cuantos):
    x= random.random()
    y= random.random()
    
    y_calculo= math.sqrt(1-x*x)
    if y>y_calculo:
        None
    else:
        cuantos_si+= 1
        
cuarto_de_area= float(cuantos_si/float(cuantos))
pi= cuarto_de_area* 4

print("El cuarto de pi es: ", cuarto_de_area)
print("El valor de pi es: ", pi)

   
