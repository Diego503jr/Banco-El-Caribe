import time
banco = [
   { 
    "codigoClientes": 10001,
    "nombreClientes": "Cesar Pilajuan", 
    "numeroCuentas": 1110001,
    "saldo": 50, 
    "retiros": [50],
    "fechaRetiros": ["15/01/2023 8:42:59"],
    "depositos": [100],
    "fechaDepositos": ["14/01/2023 7:43:01"]
    }
]

cantClientes = 0

def cargador(): #Esta funcion es un cargador
    print("\nCargando", end= " ")
    for t in range(3):
          print(" . ", end= " ")
          time.sleep(1)

def manejoErrorINT(msj): #Esta funcion maneja si en el input se ingresa tipo STR
    while True:
        try:
            value = int(input(msj))
            return value
        except ValueError:
            print("\n   --- Error! Digite numeros ---")

def manejoErrorSTR(msj): #Esta funcion maneja si en el input se ingresa tipo INT
    while True:
        value = str(input(msj))
        if value.isdigit():
            print("\n   --- Error! Digite texto ---")
        else:
            return value

print("""\n
         *****************************************************************
         *      BIENVENIDOS AL PROGRAMA DE EL BANCO EL CARIBE            *
         *****************************************************************""")  


while True:
    cargador()
    print("\nA CONTINUACIÓN SE TE PRESENTA EL MENÚ DE OPCIONES DE NUESTRO PROGRAMA: ")  
    print("\n1. Agregar cliente.")                                                     
    print("2. Agregar transacción.")
    print("3. Modificar cliente.")
    print("4. Eliminar cliente.")
    print("5. Mostrar lista de clientes con depósitos.")
    print("6. Mostrar lista de clientes con retiros.")
    print("7. Mostrar lista con clientes ordenada por Número de cuenta.")
    print("8. Salir del programa.")
    respuesta = manejoErrorINT("Ingrese la opción del menú deseada: ")

    if respuesta == 1:
        cargador()
        print("\n --- AGREGAR CLIENTE --- ")
        while True:
            cant = manejoErrorINT("\n¿Cuántos clientes desea agregar?: ") 
            for i in range(cant): #aqui recorre la cantidad de clientes que agregará
                print("\nCliente N°", cantClientes+1)
                codigoClientes = manejoErrorINT("Digite el código del cliente: ")
                nombreClientes = manejoErrorSTR("Digite el nombre del cliente: ")
                numeroCuenta = input("Digite el numero de cuenta: ")
                cliente = { #Las variables anteriores se agregaran al diccionario y los retiros y depositos iniciara como lista
                "codigoClientes": codigoClientes, 
                "nombreClientes": nombreClientes, 
                "numeroCuentas": numeroCuenta, 
                "saldo": 0, 
                "retiros": [],
                "fechaRetiros": [],
                "depositos": [],
                "fechaDepositos": []
                }
                banco.append(cliente) #Se agrega en cada reccorido el diccionario a la lista banco
                cantClientes += 1 #Este contador aparece en el sistema, sirve para recorrer los diccionarios y servira para obtener los promedios creo
            salir = manejoErrorSTR("\n¿Desea regresar al menú? \n(si/no): ") #Manda al menu principal si agrega si
            if salir.lower() == "si":
                break
            else:
                continue

    elif respuesta == 2:
        cargador()
        print("\n --- AGREGAR TRANSACCION --- ")
        #Verifica si hay clientes sino hay muestra un mensaje que no hay y lo saca porque sino hay que mas tiene que hacer aqui xd
        while True:
            codigo = manejoErrorINT("\nDigite el código de cliente: ")
            encontrado = False
            for cliente in banco:
                if cliente["codigoClientes"] == codigo: #Verifica si hay un codigo que concuerde con el cliente
                    encontrado = True
                    print("\n   --- Cliente Encontrado! ---")
                    print("Codigo Cliente: \t", cliente["codigoClientes"])
                    print("Nombre Cliente: \t", cliente["nombreClientes"])
                    print("Cuenta N°: \t\t", cliente["numeroCuentas"])
                    print("Saldo: $ \t\t", cliente["saldo"])
                    tipoTransaccionAgregar = manejoErrorINT("\n\nTipo de transacción que desea realizar:\n1- Deposito\n2- Retiro\nIngrese la opción deseada: ")
                    if tipoTransaccionAgregar == 1 :
                        print("\n - DEPOSITO - ")
                        valorDeposito = manejoErrorINT("Ingrese la cifra a depositar: $ ")
                        fechaDeposito = input("Digite la fecha de este depósito: ")
                        cliente["saldo"] += valorDeposito
                        cliente["depositos"].append(valorDeposito)
                        cliente["fechaDepositos"].append(fechaDeposito)
                        print("\n   --- ¡Su Deposito fue satisfactoriamente hecho! ---")
                        break
                    elif tipoTransaccionAgregar == 2:
                        print("\n - RETIRO -")
                        if cliente["saldo"] > 0: #Se comprueba si el saldo esta a 0 y asi no realizara el retiro
                            while True:
                                valorRetiro = manejoErrorINT("\nIngrese la cifra a depositar: $ ")
                                if valorRetiro - cliente["saldo"] <= 0: #Comprueba si el valor del retiro menos el saldo es aun menor lanza una alerta
                                    cliente["saldo"] -= valorRetiro
                                    fechaRetiro = input("Digite la fecha de este retiro: ")
                                    cliente["retiros"].append(valorRetiro)
                                    cliente["fechaRetiros"].append(fechaRetiro)
                                    print("\n   --- ¡Su Retiro fue satisfactoriamente hecho! ---")
                                    break
                                else:
                                    print("\n   --- No tiene saldo suficiente ---")
                                    continue
                        else:
                            print("\n   --- No posee saldo aún ---")
                    else:
                        print("\nPor favor ingresa una de las opciones dadas!")
            if not encontrado:
                print("\n   --- Cliente No Encontrado! ---")
                continue
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
            codigo = manejoErrorINT("\nDigite el código de cliente: ")
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

    elif respuesta == 5: #ya muestra todos los depositos pero falta corregir 
        print("\n --- Lista de clientes con sus respectivos depositos --- ") 
        for i in range (cantClientes):
            print("-----------------------------")
            print("\tCliente", i+1)
            print("\tCódigo:", clientes["codigoClientes"][i])
            print("\tNombre:", clientes["nombreClientes"][i])
            print("\tDepósitos:")
            for deposito in clientes["depositos"]:
                print("\t\t$:",deposito)
                print("-----------------------------")
            
    elif respuesta == 6: #ya muestra todos los retiros pero falta corregir
        print("\n --- Lista de clientes con sus respectivos retiros --- ") 
        for i in range (cantClientes):
            print("-----------------------------")
            print("\tCliente", i+1)
            print("\tCódigo:", clientes["codigoClientes"][i])
            print("\tNombre:", clientes["nombreClientes"][i])
            print("\tDepósitos:")
            for retiro in clientes["retiros"]:
                print("\t\t$:",retiro)
                print("-----------------------------")
    elif respuesta == 7:
        print("\n --- Lista de Clientes ordenados según número de cuenta --- ")
        # Obtener una lista de tuplas (numeroCuenta, indice) para ordenar los clientes
        # cuentas_indices = list(zip(clientes["numeroCuenta"], range(cantClientes)))
        # cuentas_indices = sorted(cuentas_indices)
        # for cuenta, indice in cuentas_indices:
        #     print("\n Cliente N°", indice + 1, "\n")
        #     print("Número de cuenta:", clientes["numeroCuenta"][indice])
        #     print("Nombre del cliente:", clientes["nombreClientes"][indice])
        #     print("Código del cliente:", clientes["codigoClientes"][indice])
        #     print("Depósitos: $", clientes["depositos"][indice])
        #     print("Retiros: $", clientes["retiros"][indice])
        #     print("Fecha de Retiro:", clientes["fechaRe"][indice])
        #     print("Fecha de Depósito:", clientes["fechaDe"][indice])
        #     print("------------------------------------------------")
        for cliente in banco:
            print("Codigo: ", cliente["codigoClientes"])
            print("Nombre: ", cliente["nombreClientes"])
            print("Cuenta: ", cliente["numeroCuentas"])
            print("Saldo: $\t", cliente["saldo"])
            #De deposito en adelante se tiene que iterar de nuevo
            print("Fechas de Depósito: \t", cliente["fechaDepositos"])
            print("Depósitos: \t\t", cliente["depositos"])
            print("Fechas de Retiro: \t", cliente["fechaRetiros"])
            print("Retiros: \t\t", cliente["retiros"])

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
