"""
Entradas
cedula-->int-->cc
dia-->int-->dia
salidas
ingreso-->str-->ingreso
"""
cc=input("Digite cedula: ")
dia=int(input("Digite Día: "))
ultimo=int(cc[-1])
if(ultimo%2==0 and dia%2!=0):
  print("Puede ingresar :)")
elif(ultimo%2!=0 and dia%2==0):
  print("puede ingresar: )")
else:
  print("no puede ingresar")
