edad = int(input("Digite su edad:"))

if (edad > 17 and edad < 50):
  print("Puede prestar el servicio militar")
  
elif(edad > 70):
  print("Esta jubilado")
  
else:
  print("No puede prestar el servicio militar")