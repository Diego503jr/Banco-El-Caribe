print("""
         *****************************************************************
         *      BIENVENIDOS AL PROGRAMA DE EL BANCO EL CARIBE            *
         *****************************************************************""")

print("\nA CONTINUACIÓN SE TE PRESENTA EL MENÚ DE OPCIONES DE NUESTRO PROGRAMA: ")

respuesta = int(input("\n 1. Agregar cliente. \n 2. Modificar cliente. \n 3. Agregar transacción. \n 4. Eliminar cliente. \n 5. Mostrar lista de clientes con depósitos. \n 6. Mostrar lista de clientes con retiros. \n 7. Mostrar lista con clientes ordenada por Número de cuenta. \n 8. Salir del programa. \n Agrega la opción del menú: "))

while i:
    if respuesta == "1":
        print("D")
    elif respuesta == "2":
        print("D")
    elif respuesta == "3":
        print("C")
    elif respuesta == "4":
        print("C")
    elif respuesta == "5":
        print("G")
    elif respuesta == "6":
        print("G")
    elif respuesta == "7":
        print("V")
    elif respuesta == "8":
        print("""\n
                  **************************************
                  *        EL BANCO EL CARIBE          *
                  **************************************""")
        print("""\n
                ********************************************
                *    HA FINALIZADO EL PROGRAMA             *
                ********************************************""")
        break
    else:
        print("Ha ingresado una opción incorrecta. Por favor ingresa una opción del menú.")
        continue 
