n1 = int(input("Digite el primer numero"))
n2 = int(input("Digite el segundo numero"))


def suma(numero1, numero2):
  return numero1 +  numero2

def resta(numero1, numero2):
  return numero1 -  numero2

def multiplicacion(numero1, numero2):
  return numero1 *  numero2

def division(numero1, numero2):
  return numero1 / numero2

def mod(numero1, numero2):
  return numero1 % numero2

print("Suma: ",suma(n1, n2))
print("Resta: ",resta(n1, n2))
print("Multiplicacion: ",multiplicacion(n1, n2))
print("División: ",division(n1, n2))
print("Modulo: ",mod(n1, n2))

