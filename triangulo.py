cadenaStr = "Python"
cadenaArr = ["P", "y", "t", "h", "o", "n"]

def recorriendoString(cadena):
  print("Lineal")
  for i in range(len(cadena)):
    print(cadena[i])
    
    
  print("En Inversa")
  print(cadena[-1])
  print(cadena[-2])
  print(cadena[-3])
  print(cadena[-4])
  print(cadena[-5])
  print(cadena[-6] ,"\n")
  
  
def recorriendoArray(arr):
  print("Lineal")
  for i in range(len(arr)):
    print(arr[i])
    
    
  print("En Inversa")
  print(arr[-1])
  print(arr[-2])
  print(arr[-3])
  print(arr[-4])
  print(arr[-5])
  print(arr[-6], "\n")

print("Recorriendo El String")
recorriendoString(cadenaStr)
print("Recorriendo el Array")
recorriendoArray(cadenaArr)