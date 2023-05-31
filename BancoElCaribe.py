clientes = {
    "codigoClientes" : [],
    "nombreClientes" : [],
    "numeroCuenta" : [],
    "retiros" : [],
    "depositos" : [],
    "fecha" : [],
    "total" : []
}
totDep = 0
totRet = 0
cantClientes = 0

print("""\n
         *****************************************************************
         *      BIENVENIDOS AL PROGRAMA DE EL BANCO EL CARIBE            *
         *****************************************************************""") #Esto lo dejé fuera del bucle 
                                                                                #para que solo aparezca una vez

while True:
    print("\nA CONTINUACIÓN SE TE PRESENTA EL MENÚ DE OPCIONES DE NUESTRO PROGRAMA: ") #Esto si esta dentro para 
    print("\n1. Agregar cliente.")                                                     #que muestre el menú siempre
    print("2. Modificar cliente.")
    print("3. Agregar transacción.")
    print("4. Eliminar cliente.")
    print("5. Mostrar lista de clientes con depósitos.")
    print("6. Mostrar lista de clientes con retiros.")
    print("7. Mostrar lista con clientes ordenada por Número de cuenta.")
    print("8. Salir del programa.")
    respuesta = int(input("Ingrese la opción del menú deseada: "))

    if respuesta == 1:
        cant = int(input("\n¿Cuántos clientes desea agregar?: ")) 
        for i in range(cant): #aqui recorre la cantidad de clientes que agregará
            print("Cliente N°", cantClientes+1)
            codigoClientes = input("Digite el código del cliente: ")
            nombreClientes = input("Digite el nombre del cliente: ")
            numeroCuenta = input("Digite el numero de cuenta: ")
            clientes["codigoClientes"].append(codigoClientes)
            clientes["nombreClientes"].append(nombreClientes)
            clientes["numeroCuenta"].append(numeroCuenta)
            cantClientes += 1 #Este contador aparece en el sistema, sirve para recorrer los diccionarios y servira para obtener los promedios creo
        salir = str(input("\n¿Desea regresar al menú?: ")) #Aquí lo saca completamente del programa
        if salir == "no":                                    #solo si escribe "no"
            break

    elif respuesta == 2: #Este se suponía que iba a hacer yo, pero me confundí e hice el punto 3 xd
        print("B")

    elif respuesta == 3: #En este si el cliente no tiene retiros o depositos, en esa parte da error :c
            codigo = input("\n\nDigite el código de cliente: ")
            for i in range(cantClientes):
                if clientes["codigoClientes"][i] == codigo:
                    print("\nCliente encontrado!")
                    print("Codigo Cliente: \t", clientes["codigoClientes"][i])
                    print("Nombre Cliente: \t", clientes["nombreClientes"][i])
                    print("Cuenta N°: \t\t", clientes["numeroCuenta"][i])
                    print()
                    while True: #Este while true esta simplemente por si selecciona una opción que no es lo regrese
                        tipoTransaccion = int(input("\n1. Depósito\n2. Retiro\nQué tipo de transacción hará: "))
                        if tipoTransaccion == 1:
                            valorDeposito = float(input("Digite la cantidad a depositar: $"))
                            totDep += valorDeposito #este sera el total total de todos los depositos
                            fecha = input("Digite la fecha de este depósito: ")
                            clientes["depositos"].append(valorDeposito)
                            clientes["fecha"].append(fecha) #la fecha realmente no supe como ocuparla xd
                            salirMenu = input("\n¿Desea realizar más transacciones?")
                            if salirMenu == "no": #si le da que no, lo regresa al menú
                                break
                        elif tipoTransaccion == 2:
                            valorRetiro = float(input("Digite la cantidad a retirar: $"))
                            totRet += valorRetiro #Este sera el total total de todos los retiros
                            fecha = input("Digite la fecha de este retiro: ")
                            clientes["retiros"].append(valorRetiro)
                            clientes["fecha"].append(fecha) #pero ya está creada xdxd
                            salirMenu = input("\n¿Desea realizar más transacciones?")
                            if salirMenu == "no": #si le da que no, lo regresa al menú
                                break
                        else:
                            print("\nOpción inválida")
                        break
                else:
                    print("Cliente no encontrado.")
        #saldoF = totDep - totRet (#Este será el total total de todos los movimientos del banco pero me falló xd)        
    
    elif respuesta == 4:
        print("Esto solo es una prueba") #Esto es para probar la impresión de datos, no es el punto 3 xdxd
        for i in range(cantClientes):
            print("Código Cliente", clientes["codigoClientes"][i])
            print("Nombre Cliente", clientes["nombreClientes"][i])
            print("N° de Cuenta", clientes["numeroCuenta"][i])
            print("Total depositos", clientes["depositos"][i])
            print("Total retiros", clientes["retiros"][i])
            print("Fechas", clientes["fecha"][i],"\n")
        print("Total: $", totDep)
        print("Total: ", totRet)
        #print("Saldo Final", saldoF) auuí mero me fallo :c

    elif respuesta == 5:
        print("G")
    elif respuesta == 6:
        print("G")
    elif respuesta == 7:
        print("V")
    elif respuesta == 8:
        print("""\n
                  **************************************
                  *         EL BANCO EL CARIBE         *
                  **************************************""")
        print("""\n
                ********************************************
                *         HA FINALIZADO EL PROGRAMA        *
                ********************************************""")
        break
    else:
        print("Ha ingresado una opción incorrecta. Por favor ingresa una opción del menú.")
        continue 
