import random

colores = ["rojo", "naranja", "amarillo"]

print("El color es:", colores[2])

seleccion = input("Escoja un numero: ")

computadora = random.randint(0,5)

if int(seleccion) == computadora:
  print("seleccionaron el mismo numero")
else:
  print("Seleccionaron diferentes numeros")

print("Opcion de la computadora ", computadora)

  

