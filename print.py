print("Hola")

print("Hola", "Adios")
print("El valor de 2 + 2 es:", 4)
print("Hola", "Jon", sep="    ") # Separacion
print("Hola", "Jon", end="!!!!\n") #Lo que va al final


with open("Prueba.txt", "w") as archivo:
  print("Viene...", file= archivo)