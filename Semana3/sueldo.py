"""
Entradas
sueldo-->float-->sueldo
Salida
Salario+aumento-->float-->aumento
"""
#Entradas
sueldo=float(input("Digite Sueldo: "))
#caja negra
if(sueldo<900_000):
  sueldo=sueldo+sueldo*0.15
else:
  sueldo=sueldo+sueldo*0.12  
#Salidas 
print("Tu sueldo es:",sueldo)
