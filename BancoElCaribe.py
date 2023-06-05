import time
print(" CALCULANDO", end= " ")
for t in range(5):
      print(" . ", end= " ")
      time.sleep(3)
#Datos quemados son esos y se pueden revisar descomentando lo que esta comentado y vicerversa con lo que no esta comentado en la opcion 
clientes = {
    "codigoClientes" : [1001,1002,1003,1004],
    "nombreClientes" : ["Diego","Gabriela","Carlos","Vladimir"],
    "numeroCuenta" : [111001,111002,111003,111004,],
    "retiros" : [100,200,300,400],
    "depositos" : [1000,2000,3000,4000],
    "fechaRe" : ["12/01/23","13/01/23","14/01/23","14/01/23"],
    "fechaDe" : ["12/01/23","13/01/23","14/01/23","14/01/23"],
}
totDep = 0
totRet = 0
cantClientes = 4

#Esta funcion lo que hace es manejar el error si se escribe Strings muestra el error que no es un valor numerico
def manejoErrorOpcion(msj):
    while True:
        try:
            value = int(input(msj))
            return value
        except ValueError:
            print("\n   --- Error! Digite valores numericos ---")

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
    respuesta = manejoErrorOpcion("Ingrese la opción del menú deseada: ")

    if respuesta == 1:
        while True:
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
            if salir == "si":                                    #solo si escribe "no"
                break

    elif respuesta == 2:
        print("\n --- AGREGAR TRANSACCION --- ")
        #Verifica si hay clientes sino hay muestra un mensaje que no hay y lo saca porque sino hay que mas tiene que hacer aqui xd
        while True:
            codigo = manejoErrorOpcion("\nDigite el código de cliente: ")
            encontrado = False
            for i in range(cantClientes):
                #Verifica si hay un codigo que concuerde con el cliente
                if clientes["codigoClientes"][i] == codigo:
                    encontrado = True
                    print("\n   --- Cliente Encontrado! ---")
                    print("Codigo Cliente: \t", clientes["codigoClientes"][i])
                    print("Nombre Cliente: \t", clientes["nombreClientes"][i])
                    print("Cuenta N°: \t\t", clientes["numeroCuenta"][i])
                    #Aun no sirve el agregar porque esta complejo esto xd
                    tipoTransaccionAgregar = manejoErrorOpcion("\n\nTipo de transacción que desea realizar:\n1- Deposito\n2- Retiro\nIngrese la opción deseada: ")
                    if tipoTransaccionAgregar == 1 :
                        print("\n - DEPOSITO - ")
                        valorDeposito = manejoErrorOpcion("Ingrese la cifra a depositar: $ ")
                        clientes["depositos"].append(valorDeposito)
                        totDep += valorDeposito
                        fechaDeposito = input("Digite la fecha de este depósito: ")
                        clientes["depositos"].append(valorDeposito)
                        clientes["fechaDe"].append(fechaDeposito)
                        print("\n   --- ¡Su Deposito fue satisfactoriamente hecho! ---")
                    elif tipoTransaccionAgregar == 2:
                        print("\n - RETIRO -")
                        valorRetiro = manejoErrorOpcion("\nIngrese la cifra a depositar: $ ")
                        clientes["retiros"].append(valorRetiro)
                        totRet += valorRetiro
                        fechaRetiro = input("Digite la fecha de este retiro: ")
                        clientes["retiros"].append(valorRetiro)
                        clientes["fechaRe"].append(fechaRetiro)
                        print("\n   --- ¡Su Retiro fue satisfactoriamente hecho! ---")
                    else:
                        print("\nPor favor ingresa una de las opciones dadas!")
            if not encontrado:
                print("\n   --- Cliente No Encontrado! ---")
                continue
            saldoF = totDep - totRet
            break

    elif respuesta == 3: #En este si el cliente no tiene retiros o depositos, en esa parte da error :c
        cant=int(input("¿Cuántos clientes desea modificar?")) #ver la cantidad de clientes a modificar 
        for i in range (cant):
            while True:
                codigo=int(input("Ingrese el código del cliente a modificar: "))
                if codigo in clientes["codigoClientes"]: #si el codigo ingresado existe en el diccionario clientes proecede a buscarlo por su indice 
                    index = clientes["codigoClientes"].index(codigo)
                    print("Cliente encontrado!")
                    print("Código del cliente:",clientes["codigoClientes"][index]) #para trabajar las modificaciones se accede por el indice 
                    print("Nombre del cliente:",clientes["nombreClientes"][index])
                    print("Cuenta del cliente:",clientes["numeroCuenta"][index])

                    nuevoCodigo=int(input("Ingrese el nuevo codigo del cliente: "))
                    nuevoNombre=input("Ingrese el nuevo nombre del cliente: ")
                    nuevaCuenta=int(input("Ingrese el nuevo número de cuenta del cliente: "))

                    clientes["codigoClientes"][index]= nuevoCodigo #se asigna un nuevo valor al diccionario por medio del indice en la lista 
                    clientes["nombreClientes"][index]= nuevoNombre
                    clientes["numeroCuenta"][index]= nuevaCuenta

                    print("El cliente ha sido modificado con exito!")
                    break
                else:
                    print("Cliente no encontrado")

    elif respuesta == 4:
        print("\n --- ELIMINAR CLIENTE --- ")
        #Verifica si hay clientes sino hay muestra un mensaje que no hay y lo saca porque sino hay que mas tiene que hacer aqui xd
        while True:
            codigo = manejoErrorOpcion("\nDigite el código de cliente: ")
            encontrado = False
            for i in range(cantClientes):
                #Aqui aun no se elimina solo esta como demostracion esta complejo el bolado xd
                if clientes["codigoClientes"][i] == codigo:
                    encontrado = True
                    print("\n   --- Cliente Encontrado! ---")
                    print("\nCodigo Cliente: \t", clientes["codigoClientes"][i])
                    print("Nombre Cliente: \t", clientes["nombreClientes"][i])
                    print("Cuenta N°: \t\t", clientes["numeroCuenta"][i])
                    confirmation = input("\n¿Deseas eliminar el cliente? (si/no): ")
                    if confirmation.lower() == "si":
                        clientes["codigoClientes"].pop(i)
                        clientes["nombreClientes"].pop(i)
                        clientes["numeroCuenta"].pop(i)
                        clientes["depositos"].pop(i)
                        clientes["retiros"].pop(i)
                        clientes["fechaDe"].pop(i)
                        clientes["fechaRe"].pop(i)
                        cantClientes -= 1
                        print("\n   --- Se elimino el cliente ---")
                    elif confirmation.lower() == "no":
                        print("\n   --- No se elimino el cliente ---")
                    else:
                        print("\nHa ingresado una opción incorrecta. Por favor ingresa una opción del submenú.")
            if not encontrado:
                print("\n   --- Cliente No Encontrado! ---")
                continue
            break

    elif respuesta == 5:
        print("Lista de clientes con sus respectivos depositos:")
        for i in range(cantClientes):
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
         print("\n --- Lista de Clientes ordenados según número de cuenta --- ")
        # Obtener una lista de tuplas (numeroCuenta, indice) para ordenar los clientes
        cuentas_indices = list(zip(clientes["numeroCuenta"], range(cantClientes)))
        cuentas_indices = sorted(cuentas_indices)
        for cuenta, indice in cuentas_indices:
            print("\n Cliente N°", indice + 1, "\n")
            print("Número de cuenta:", clientes["numeroCuenta"][indice])
            print("Nombre del cliente:", clientes["nombreClientes"][indice])
            print("Código del cliente:", clientes["codigoClientes"][indice])
            print("Depósitos: $", clientes["depositos"][indice])
            print("Retiros: $", clientes["retiros"][indice])
            print("Fecha de Retiro:", clientes["fechaRe"][indice])
            print("Fecha de Depósito:", clientes["fechaDe"][indice])
            print("------------------------------------------------")
    elif respuesta == 8:
        print("""\n
                ***********************************************
                *          HA FINALIZADO EL PROGRAMA          *
                ***********************************************""")
        print("""\n
                *******************************************************
                *       GRACIAS POR UTILIZAR NUESTRO PROGRAMA         *
                *******************************************************""")
        break
    else:
        print("\n Ha ingresado una opción incorrecta, por favor ingresa las opciones del menú.")
        continue
