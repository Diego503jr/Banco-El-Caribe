#Lista para eliminar el cliente de una vez //se supone que aquí se añadira el diccionario cliente xd
listaClientes = []
clientes = {
    "codigoClientes" : [12345],
    "nombreClientes" : ["Diego"],
    "numeroCuenta" : [123456],
    "retiros" : [2],
    "depositos" : [3],
    "fechaRe" : ["12/03/23"],
    "fechaDe" : ["12/03/23"],
    "total" : [1233]
}
totDep = 0
totRet = 0
cantClientes = 1

#Esta funcion lo que hace es manejar el error si se escribe Strings muestra el error que no es un valor numerico
def manejoErrorOpcion(msj):
    while True:
        try:
            value = int(input(msj))
            return value
        except ValueError:
            print("Error! Digite valores numericos")

print("""\n
         *****************************************************************
         *      BIENVENIDOS AL PROGRAMA DE EL BANCO EL CARIBE            *
         *****************************************************************""") #Esto lo dejé fuera del bucle 
                                                                                #para que solo aparezca una vez

while True:
    print("\nA CONTINUACIÓN SE TE PRESENTA EL MENÚ DE OPCIONES DE NUESTRO PROGRAMA: ") #Esto si esta dentro para 
    print("\n1. Agregar cliente.")                                                     #que muestre el menú siempre
    print("2. Agregar transacción.")
    print("3. Modificar cliente.")
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
        salir = str(input("\n\n¿Desea regresar al menú?: ")) #Aquí lo saca completamente del programa
        if salir == "no":                                    #solo si escribe "no"
            break

    elif respuesta == 2:
        print("\n --- AGREGAR TRANSACCION --- ")
        while True:
            respuesta = manejoErrorOpcion("\nEscoja una opcion \n1.Seguir \n2.Regresar:\nIngrese la opción deseada: ")
            if respuesta == 1:
                #Verifica si hay clientes sino hay muestra un mensaje que no hay y lo saca porque sino hay que mas tiene que hacer aqui xd
                if cantClientes > 0:
                    codigo = manejoErrorOpcion("\nDigite el código de cliente: ")
                    for i in range(cantClientes):
                        #Verifica si hay un codigo que concuerde con el cliente
                        if clientes["codigoClientes"][i] == codigo:
                            print("\n   --- Cliente Encontrado! ---")
                            print("Codigo Cliente: \t", clientes["codigoClientes"][i])
                            print("Nombre Cliente: \t", clientes["nombreClientes"][i])
                            print("Cuenta N°: \t\t", clientes["numeroCuenta"][i])
                            #Aun no sirve el agregar porque esta complejo esto xd
                            tipoTransaccionAgregar = manejoErrorOpcion("\n\nTipo de transacción que desea realizar:\n1- Deposito\n2- Retiro\n3- Regresar al submenú\nIngrese la opción deseada: ")
                            if tipoTransaccionAgregar == 1 :

                                print("\n - DEPOSITO - ")
                                valorDeposito = manejoErrorOpcion("Ingrese la cifra a depositar: $ ")
                                clientes["depositos"].append(valorDeposito)
                                totDep += valorDeposito
                                fechaDeposito = input("Digite la fecha de este depósito: ")
                                clientes["depositos"].append(valorDeposito)
                                clientes["fechaDe"].append(fechaDeposito)

                                tipoTransaccionAgregar = manejoErrorOpcion("\n3- Regresar al submenu\nIngrese la opción: ")

                            elif tipoTransaccionAgregar == 2:

                                print("\n - RETIRO -")
                                valorRetiro = manejoErrorOpcion("\nIngrese la cifra a depositar: $ ")
                                clientes["retiros"].append(valorRetiro)
                                totRet += valorRetiro
                                fechaRetiro = input("Digite la fecha de este retiro: ")
                                clientes["retiros"].append(valorRetiro)
                                clientes["fechaRe"].append(fechaRetiro)

                                tipoTransaccionAgregar = manejoErrorOpcion("\n3- Regresar al submenu\nIngrese la opción: ")

                            elif tipoTransaccionAgregar == 3:
                                break
                            else:
                                print("\nPor favor ingresa una de las opciones dadas!")
                        else:
                            print("\n   --- Cliente No Encontrado! ---")
                    saldoF = totDep -totRet
                else:
                    print("\n   --- No hay clientes ---")  
                    break
            elif respuesta == 2:
                break
            else:
                print("\nHa ingresado una opción incorrecta. Por favor ingresa una opción del submenú.")
                
    elif respuesta == 3: #En este si el cliente no tiene retiros o depositos, en esa parte da error :c
            codigo = input("\nDigite el código de cliente: ")
            # for i in range(cantClientes):
            #     if clientes["codigoClientes"][i] == codigo:
            #         print("\nCliente encontrado!")
            #         print("Codigo Cliente: \t", clientes["codigoClientes"][i])
            #         print("Nombre Cliente: \t", clientes["nombreClientes"][i])
            #         print("Cuenta N°: \t\t", clientes["numeroCuenta"][i])
            #         print()
            #         while True: #Este while true esta simplemente por si selecciona una opción que no es lo regrese
            #             tipoTransaccion = int(input("\n1. Depósito\n2. Retiro\nQué tipo de transacción hará: "))
            #             if tipoTransaccion == 1:
            #                 valorDeposito = float(input("Digite la cantidad a depositar: $"))
            #                 totDep += valorDeposito #este sera el total total de todos los depositos
            #                 fecha = input("Digite la fecha de este depósito: ")
            #                 clientes["depositos"].append(valorDeposito)
            #                 clientes["fecha"].append(fecha) #la fecha realmente no supe como ocuparla xd
            #                 salirMenu = input("\n¿Desea realizar más transacciones?")
            #                 if salirMenu == "no": #si le da que no, lo regresa al menú
            #                     break
            #             elif tipoTransaccion == 2:
            #                 valorRetiro = float(input("Digite la cantidad a retirar: $"))
            #                 totRet += valorRetiro #Este sera el total total de todos los retiros
            #                 fecha = input("Digite la fecha de este retiro: ")
            #                 clientes["retiros"].append(valorRetiro)
            #                 clientes["fecha"].append(fecha) #pero ya está creada xdxd
            #                 salirMenu = input("\n¿Desea realizar más transacciones?")
            #                 if salirMenu == "no": #si le da que no, lo regresa al menú
            #                     break
            #             else:
            #                 print("\nOpción inválida")
            #             break
            #     else:
            #         print("Cliente no encontrado.")
       # saldoF = totDep - totRet (Este será el total total de todos los movimientos del banco pero me falló xd)        

    elif respuesta == 4:
        print("\n --- ELIMINAR CLIENTE --- ")
        while True:
            respuesta = manejoErrorOpcion("\nEscoja una opcion \n1.Seguir \n2.Regresar:\nIngrese la opción deseada: ")
            if respuesta == 1:
                #Verifica si hay clientes sino hay muestra un mensaje que no hay y lo saca porque sino hay que mas tiene que hacer aqui xd
                if cantClientes > 0:
                    codigo = manejoErrorOpcion("\nDigite el código de cliente: ")
                    for i in range(cantClientes):
                        print("\n   --- Cliente Encontrado! ---")
                        print("\nCodigo Cliente: \t", clientes["codigoClientes"][i])
                        print("Nombre Cliente: \t", clientes["nombreClientes"][i])
                        print("Cuenta N°: \t\t", clientes["numeroCuenta"][i])
                        #Aqui aun no se elimina solo esta como demostracion esta complejo el bolado xd
                        if clientes["codigoClientes"][i] == codigo:
                            confirmation = input("\n¿Deseas eliminar el cliente? (si/no): ")
                            if confirmation.lower() == "si":
                                # clientes["codigoClientes"].remove(codigoClientes)
                                # clientes["nombreClientes"].remove(nombreClientes)
                                # clientes["numeroCuenta"].remove(numeroCuenta)
                                print("\n   --- Se borro el cliente ---")
                                break
                            elif confirmation.lower() == "no":
                                print("\n   --- No se borro el cliente ---")
                                break
                            else:
                                print("\nHa ingresado una opción incorrecta. Por favor ingresa una opción del submenú.")
                        else:
                            print("\n   --- Cliente No Encontrado! ---")
                else:
                    print("\n   --- No hay clientes ---")
                    break
            elif respuesta == 2:
                break
            else:
                print("\nHa ingresado una opción incorrecta. Por favor ingresa una opción del submenú.")

    elif respuesta == 5:
        print("Lista de clientes con sus respectivos depositos:")
        print("\n Cliente", i+1, "\n")
        print("Codigo del cliente: ", clientes["codigoClientes"][i])
        print("Nombre del cliente: ", clientes["nombreClientes"][i])
        print("Número de cuenta:", clientes["numeroCuenta"][i])
        print("Depositos: $ ", clientes["depositos"][i])
    elif respuesta == 6:
        print("Lista de clientes con sus respectivos rertiros:")
        for i in range (cantClientes):
            print("\n Cliente", i+1, "\n")
            print("Codigo del cliente: ", clientes["codigoClientes"][i])
            print("Nombre del cliente: ", clientes["nombreClientes"][i])
            print("Número de cuenta:", clientes["numeroCuenta"][i])
            print("Retiros: $ ", clientes["retiros"][i])
    elif respuesta == 7:
        print("V")
    elif respuesta == 8:
        print("""\n
                  **************************************
                  *        EL BANCO EL CARIBE          *
                  **************************************""")
        while True:
            try:
                respuesta = input("\n¿Desea salir del programa? si/no: ")
                if not respuesta.lower()in ["si", "no"]:
                    raise ValueError ("\nPor favor, ingrese ´si´ o ´no´.")
                print("""\n
                ********************************************
                *        HA FINALIZADO EL PROGRAMA         *
                ********************************************""")
                break
            except ValueError as e:
                print(e)
                if respuesta.lower()=="si":
                    print("""\n
                ********************************************
                *        HA FINALIZADO EL PROGRAMA         *
                ********************************************""")


        
