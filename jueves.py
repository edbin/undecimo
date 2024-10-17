def suma(x, y):
    return x + y

# This function subtracts two numbers
def resta(x, y):
    return x - y

# This function multiplies two numbers
def multiplicar(x, y):
    return x * y

# This function divides two numbers
def division(x, y):
    return x / y


print("Seleccione una opcion.")
print("1.Suma")
print("2.Resta")
print("3.Multiplicar")
print("4.Dividir")

while True:
    # take input from the user
    opcion = input("opciones (1/2/3/4):")
    print("\n")

    # check if choice is one of the four options
    if opcion in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
        except ValueError:
            print("Opcion invalida. Seleccione un numero.")
            continue

        if opcion == '1':
            print(num1, "+", num2, "=", suma(num1, num2))

        elif opcion == '2':
            print(num1, "-", num2, "=", resta(num1, num2))

        elif opcion == '3':
            print(num1, "*", num2, "=", multiplicar(num1, num2))

        elif opcion == '4':
            print(num1, "/", num2, "=", division(num1, num2))
        

        siguiente = input("Otra operacion? (si/no): ")
        if siguiente == "no":
          break
    else:
        print("Opcion invalida")
