import time
import datetime #para poder agregar la fecha y hora 
banco = [
    {
    "codigoClientes": 10001,
    "nombreClientes": "Cesar Pilajuan", 
    "numeroCuentas": 100010,
    "saldo": 50, 
    "retiros": [50],
    "horayfecha_Retiros": ["2022-01-14 7:43:15"], #para agregar la fecha y hora actuales 
    "depositos": [100],
    "horayfecha_Depositos": ["2023-01-14 7:43:15"] #para agregar la fecha y hora actuales 
    }
]
cantClientes = 1

def cargador(): #Esta funcion es un cargador
    print("\nCargando", end= " ")
    for t in range(3):
          print(" . ", end= " ")
          time.sleep(0.5)
    print("\n")

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
    print("A CONTINUACIÓN SE TE PRESENTA EL MENÚ DE OPCIONES DE NUESTRO PROGRAMA: ")  
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
        print(" --- AGREGAR CLIENTE --- ")
        while True:
            cant = manejoErrorINT("\n¿Cuántos clientes desea agregar?: ")
            for i in range(cant): #aqui recorre la cantidad de clientes que agregará
                #Verifica si el codigo existe
                codigoExiste = False
                cuentaExiste = False
                #Este while hace que si no se cumple algo sigue solicitando hasta que sea verdadero todo sale
                while True:
                    print("\nCliente N°", cantClientes+1)
                    codigoClientes = manejoErrorINT("\tDigite el código del cliente: ")
                    nombreClientes = manejoErrorSTR("\tDigite el nombre del cliente: ")
                    numeroCuenta = manejoErrorINT("\tDigite el numero de cuenta: ")
                    for cliente in banco:
                        if cliente["codigoClientes"] == codigoClientes:
                            codigoExiste = True
                            break
                        elif cliente["numeroCuentas"] == numeroCuenta:
                            cuentaExiste = True
                            break
                    
                    if not codigoExiste and not cuentaExiste:
                        break
                    
                    if cuentaExiste:
                        print("\n    --- La cuenta ya la posee otro cliente ---")
                        cuentaExiste = False

                    if codigoExiste:
                        print("\n   --- El codigo ya lo posee otro cliente ---")
                        codigoExiste = False 

                #Las variables anteriores se agregaran al diccionario y los retiros y depositos iniciara como lista
                cliente = {
                    "codigoClientes": codigoClientes,
                    "nombreClientes": nombreClientes,
                    "numeroCuentas":   numeroCuenta,
                    "saldo":                0,
                    "retiros":[],
                    "horayfecha_Retiros":[],
                    "depositos":[],
                    "horayfecha_Depositos":[]
                }
                banco.append(cliente) #Se agrega en cada reccorido el diccionario a la lista banco
                cantClientes += 1 #Este contador aparece en el sistema, sirve para recorrer los diccionarios y servira para obtener los promedios creo
            continuar = manejoErrorSTR("\n¿Desea continuar? \n(si/no): ") #Manda al menu principal si agrega si
            if continuar.lower() == "si":
                continue
            else:
                break

    elif respuesta == 2:
        cargador()
        if cantClientes > 0:
            print(" --- AGREGAR TRANSACCION --- ")
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
                            horayfecha = datetime.datetime.now() 
                            formato_fecha= horayfecha.strftime("%Y-%m-%d %H:%M:%S")
                            print("Fecha y hora del depósito realizado:", formato_fecha) #para agregar la fecha y hora actuales 
                            cliente["saldo"] += valorDeposito
                            cliente["depositos"].append(valorDeposito)
                            cliente["horayfecha_Depositos"].append(formato_fecha)
                            print("\n   --- ¡Su Deposito fue satisfactoriamente hecho! ---")
                            break
                        elif tipoTransaccionAgregar == 2:
                            print("\n - RETIRO -")
                            if cliente["saldo"] > 0: #Se comprueba si el saldo esta a 0 y asi no realizara el retiro
                                while True:
                                    valorRetiro = manejoErrorINT("\nIngrese la cifra a depositar: $ ")
                                    if valorRetiro - cliente["saldo"] <= 0: #Comprueba si el valor del retiro menos el saldo es aun menor lanza una alerta
                                        cliente["saldo"] -= valorRetiro
                                        horayfecha = datetime.datetime.now() 
                                        formato_fecha= horayfecha.strftime("%Y-%m-%d %H:%M:%S") #para agregar la fecha y hora actuales 
                                        print("Fecha y hora del retiro realizado:", formato_fecha)
                                        cliente["retiros"].append(valorRetiro)
                                        cliente["horayfecha_Retiros"].append(formato_fecha)
                                        print("\n   --- ¡Su Retiro fue satisfactoriamente hecho! ---")
                                        break
                                    else:
                                        print("\n   --- No tiene saldo suficiente ---")
                                        continue
                            else:
                                print("\n   --- No posee saldo este cliente ---")
                        else:
                            print("\nPor favor ingresa una de las opciones dadas!")
                if not encontrado:
                    print("\n   --- Cliente No Encontrado! ---")
                    continue
                break
        else:
            print("   --- No hay clientes ---")
    elif respuesta == 3:
        cargador()
        if cantClientes > 0:
            print(" --- MODIFICAR CLIENTE --- ")
            cant=manejoErrorINT("\n¿Cuántos clientes desea modificar? ") #ver la cantidad de clientes a modificar 
            for i in range (cant):
                while True:
                    codigo = manejoErrorINT("Ingrese el código del cliente a modificar: ")
                    encontrado = False
                    for cliente_actual in banco:
                        if cliente_actual["codigoClientes"] == codigo:
                            encontrado = True
                            print("\nCLIENTE ENCONTRADO!")
                            print("Código del cliente:", cliente_actual["codigoClientes"])
                            print("Nombre del cliente:", cliente_actual["nombreClientes"])
                            print("Cuenta del cliente:", cliente_actual["numeroCuentas"])

                            nuevoCodigo = manejoErrorINT("\tIngrese el nuevo código del cliente: ")
                            nuevoNombre = manejoErrorSTR("\tIngrese el nuevo nombre del cliente: ")
                            nuevaCuenta = manejoErrorINT("\tIngrese el nuevo número de cuenta del cliente: ")
                            print()

                            cliente_actual["codigoClientes"] = nuevoCodigo
                            cliente_actual["nombreClientes"] = nuevoNombre
                            cliente_actual["numeroCuentas"] = nuevaCuenta

                            print("El cliente ha sido modificado con éxito!")
                            break
                    else:
                        print("Cliente no encontrado")
                        break
                    break
        else:
            print("   --- No hay clientes ---")

    elif respuesta == 4:
        cargador()
        if cantClientes > 0:
            print(" --- ELIMINAR CLIENTE --- ")
            #Verifica si hay clientes sino hay muestra un mensaje que no hay y lo saca porque sino hay que mas tiene que hacer aqui xd
            while True:
                codigo = manejoErrorINT("\nDigite el código de cliente: ")
                encontrado = False
                for indice, cliente in enumerate(banco):
                    if cliente["codigoClientes"] == codigo:
                        encontrado = True
                        print("\n   --- Cliente Encontrado! ---")
                        print("\nCodigo Cliente: \t", cliente["codigoClientes"])
                        print("Nombre Cliente: \t", cliente["nombreClientes"])
                        print("Cuenta N°: \t\t", cliente["numeroCuentas"])
                        confirmation = input("\n¿DESEA ELIMINAR EL CLIENTE? (si/no): ")
                        if confirmation.lower() == "si":
                            for cliente in banco:
                                banco.pop(indice)
                                cantClientes -= 1
                                print("\n   --- Se elimino el cliente correctamente ---")
                        elif confirmation.lower() == "no":
                            print("\n   --- No se elimino el cliente ---")
                        else:
                            print("\nHa ingresado una opción incorrecta. Por favor ingresa una opción del submenú.")
                if not encontrado:
                    print("\n   --- Cliente No Encontrado! ---")
                    continue
                break
        else:
            print("   --- No hay clientes ---")
            
    elif respuesta == 5:  
        cargador()
        if cantClientes > 0:
            print(" --- LISTA DE CLIENTES CON SUS RESPECTIVOS DEPOSITOS --- ") 
            for cliente in (banco):
                if len(cliente["depositos"]) > 0: #si el cliente no ha realizado depositos no se mostrara en la lista
                    print("-------------------------------------------------------------------------------")
                    print("\t\tCódigo:", cliente["codigoClientes"])
                    print("\t\tNombre:", cliente["nombreClientes"])
                    print("\t\tSaldo: $ ", cliente["saldo"])
                    for i in range(len(cliente["depositos"])): #para que se muestren los depositos sin el formato de lista 
                        print("\t\tDepósito", i + 1, ": $", cliente["depositos"][i])
                        print("\t\tFecha y hora del depósito realizado:", cliente["horayfecha_Depositos"][i])
        else:
            print("   --- No hay clientes ---")

    elif respuesta == 6: 
        cargador()
        if cantClientes > 0:
            print(" --- LISTA DE CLIENTES CON SUS RESPECTIVOS RETIROS --- ") 
            for cliente in (banco):
                if len(cliente["retiros"]) > 0: #si el cliente no ha realizado retiros no se mostrara en la lista 
                    print("----------------------------------------------------------------------------")
                    print("\t\tCódigo:", cliente["codigoClientes"])
                    print("\t\tNombre:", cliente["nombreClientes"])
                    print("\t\tSaldo: $", cliente["saldo"])
                    for i in range(len(cliente["retiros"])): #para que se muestren los depositos sin el formato de lista 
                        print("\t\tRetiros", i + 1, ": $", cliente["retiros"][i])
                        print("\t\tFecha y hora del retiro realizado:", cliente["horayfecha_Retiros"][i])
        else:
            print("   --- No hay clientes ---")

    elif respuesta == 7:
        cargador()
        if cantClientes > 0:
            print("-------------------------------------- LISTA DE CLIENTES ORDENADA SEGÚN NÚMERO DE CUENTA ------------------------------------")
            print("\n-----------------------------------------------------------------------------------------------------------------------------")
            print("{:<10s} {:<15s} {:<15s} {:<15s} {:<15s} {:<20s} {:<11s}".format(
                "Cliente N°", "Cuenta", "Código", "Nombre", "Saldo", "Depósitos", "Retiros"))
            print("-----------------------------------------------------------------------------------------------------------------------------")
            banco_ordenado = sorted(banco, key=lambda cliente: int(cliente["numeroCuentas"]))
            for i, cliente in enumerate(banco_ordenado, start=1):
                saldo = cliente["saldo"]
                depositos = sum(cliente["depositos"])
                retiros = sum(cliente["retiros"])
                print("{:<10d} {:<15s} {:<15s} {:<15s} ${:<14,.2f} ${:<20,.2f} ${:<10,.2f}".format(
                    i,
                    str(cliente["numeroCuentas"]),
                    str(cliente["codigoClientes"]),
                    cliente["nombreClientes"],
                    saldo,
                    depositos,
                    retiros,
                ))
                print("-----------------------------------------------------------------------------------------------------------------------------")
        else:
            print("   --- No hay clientes ---")
    elif respuesta == 8:
        cargador()
        print("""
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
