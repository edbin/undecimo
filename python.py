# CALCULARADORA

dato1 = int(input("Ingrese el primer valor "))
dato2 = int(input("Ingrese el segudo valor "))

opcion = input("1 - Suma, 2- Resta, 3- Multiplica, 4- Divide: ")
resultado = 0

if opcion == "1":
    print("Sera una suma")
    resultado = dato1 + dato2
    print(resultado)
elif opcion == "2": 
    print("Sera una resta")
    resultado = dato1 - dato2
    print(resultado)    
elif opcion == "3":
    print("Sera una multicplicacion")
    resultado = dato1 * dato2
    print(resultado)    
elif opcion == "4":
    print("Sera una division")
    resultado = dato1 / dato2
    print(resultado)
else:
    print("Opcion incorrecta!")
        
