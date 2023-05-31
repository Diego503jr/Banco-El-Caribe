print("""\n
         *****************************************************************
         *      BIENVENIDOS AL PROGRAMA DE EL BANCO EL CARIBE            *
         *****************************************************************""")

print("\nA CONTINUACIÓN SE TE PRESENTA EL MENÚ DE OPCIONES DE NUESTRO PROGRAMA: ")

print("\n1. Agregar cliente.")
print("2. Modificar cliente.")
print("3. Agregar transacción.")
print("4. Eliminar cliente.")
print("5. Mostrar lista de clientes con depósitos.")
print("6. Mostrar lista de clientes con retiros.")
print("7. Mostrar lista con clientes ordenada por Número de cuenta.")
print("8. Salir del programa.")

respuesta = int(input("Ingrese la opción del menú deseada: "))

while True:
    if respuesta == 1:
        print("D")
    elif respuesta == 2:
        print("D")
    elif respuesta == 3:
        print("C")
    elif respuesta == 4:
        print("C")
    elif respuesta == 5:
        print("G")
    elif respuesta == 6:
        print("G")
    elif respuesta == 7:
        print("V")
    elif respuesta == 8:
        print("""\n
                  **************************************
                  *        EL BANCO EL CARIBE          *
                  **************************************""")
        print("""\n
                ********************************************
                *        HA FINALIZADO EL PROGRAMA         *
                ********************************************""")
        break
    else:
        print("Ha ingresado una opción incorrecta. Por favor ingresa una opción del menú.")
        continue 
