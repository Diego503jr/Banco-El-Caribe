import time
import datetime #para poder agregar la fecha y hora 
banco = [
    {
    "codigoClientes": 10001,
    "nombreClientes": "Cesar Calderón", 
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
    respuesta = manejoErrorINT("\nIngrese la opción del menú deseada: ")

    if respuesta == 1:
        cargador()
        print(" --- AGREGAR CLIENTE --- ")
        while True:            
            print("\nSi desea cancelar y salir presione 0, seguido de Enter")
            cant = manejoErrorINT("Ingrese el numero de clientes que desea agregar?: ")
            if cant > 5:
                print("\n   --- Solo se pueden agregar 5 clientes ---")
                continue
            elif cant == 0:
                break
            for i in range(cant): #aqui recorre la cantidad de clientes que agregará
                #Verifica si el codigo existe
                codigoExiste = False
                cuentaExiste = False
                #Este while hace que si no se cumple algo sigue solicitando hasta que sea verdadero todo sale
                while True:

                    print("\n\tCliente N°", cantClientes+1)
                    codigoClientes = manejoErrorINT("\tDigite el código del cliente: ")
                    nombreClientes = manejoErrorSTR("\tDigite el nombre del cliente: ")
                    numeroCuenta = manejoErrorINT("\tDigite el numero de cuenta: ")
                    
                    for cliente in banco: #Busca si hay cuenta y codigo en vigencia 
                        if cliente["codigoClientes"] == codigoClientes:
                            codigoExiste = True
                            break
                        elif cliente["numeroCuentas"] == numeroCuenta:
                            cuentaExiste = True
                            break 

                    if not codigoExiste and not cuentaExiste: #si codigo y cuenta no existen se realiza la operacion
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
                    "saldo":0,
                    "retiros":[],
                    "horayfecha_Retiros":[],
                    "depositos":[],
                    "horayfecha_Depositos":[]
                }
                banco.append(cliente) #Se agrega en cada reccorido el diccionario a la lista banco
                cantClientes += 1 #Este contador aparece en el sistema, sirve para recorrer los diccionarios y servira para obtener los promedios creo
                continue

    elif respuesta == 2:
        cargador()
        if cantClientes > 0:
            print(" --- AGREGAR TRANSACCIÓN --- ")
            #Verifica si hay clientes sino hay muestra un mensaje que no hay y lo saca porque sino hay que mas tiene que hacer aqui xd
            while True:
                print("\nSi desea cancelar y salir presione 0, seguido de Enter")
                codigo = manejoErrorINT("Ingrese el código del cliente a modificar: ")
                encontrado = False
                if codigo == 0: # opcion para que salga del bucle si quiere
                    break
                
                for cliente in banco:
                    if cliente["codigoClientes"] == codigo: #Verifica si hay un codigo que concuerde con el cliente
                        encontrado = True
                        print("\n   --- ¡CLIENTE ENCONTRADO! ---")
                        print("\nCodigo cliente: \t", cliente["codigoClientes"])
                        print("Nombre cliente: \t", cliente["nombreClientes"])
                        print("Cuenta del cliente: \t\t", cliente["numeroCuentas"])
                        print("Saldo: $ \t\t", cliente["saldo"])

                        tipoTransaccionAgregar = manejoErrorINT("\nIngrese el tipo de transacción que desea realizar:\n1- Deposito\n2- Retiro\nIngrese la opción deseada: ")
                        if tipoTransaccionAgregar == 1 :
                            print("\n - DEPOSITO - ")
                            
                            valorDeposito = manejoErrorINT("\n\tIngrese la cifra a depositar: $ ")
                            horayfecha = datetime.datetime.now() #especifica la hora de la operacion realizada
                            formato_fecha= horayfecha.strftime("%Y-%m-%d %H:%M:%S")
                            print("\tFecha y hora del depósito realizado:", formato_fecha) #para agregar la fecha y hora actuales 
                            
                            cliente["saldo"] += valorDeposito
                            cliente["depositos"].append(valorDeposito)
                            cliente["horayfecha_Depositos"].append(formato_fecha)
                            
                            print("\n   --- ¡Su Deposito fue satisfactoriamente hecho! ---")
                            break
                        
                        elif tipoTransaccionAgregar == 2:
                            print("\n - RETIRO -")
                            if cliente["saldo"] > 0: #Se comprueba si el saldo esta a 0 y asi no realizara el retiro
                                while True:
                                    valorRetiro = manejoErrorINT("\tIngrese la cifra a depositar: $ ") 
                                    if valorRetiro - cliente["saldo"] <= 0: #Comprueba si el valor del retiro menos el saldo es aun menor lanza una alerta
                                        
                                        horayfecha = datetime.datetime.now() 
                                        formato_fecha= horayfecha.strftime("%Y-%m-%d %H:%M:%S") #establecer que se mostrara años, meses, dias 
                                        print("\tFecha y hora del retiro realizado:", formato_fecha)
                                        
                                        cliente["saldo"] -= valorRetiro
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
            print("\n --- MODIFICAR CLIENTE --- ")

        while True:
            cant = manejoErrorINT("\n¿Cuántos clientes desea modificar? ")
            if cant > 5:
                print("\n   --- Solo se pueden modificar 5 clientes ---")
                continue
            else:
                break

        for i in range(cant):
            while True:
                print("\nSi desea cancelar y salir presione 0, seguido de Enter")
                codigo = manejoErrorINT("Ingrese el código del cliente a modificar: ")
                codigoExiste = False  #Para verificar si el código existe
                if codigo == 0:
                    break
                for cliente_actual in banco:
                    if cliente_actual["codigoClientes"] == codigo:
                        codigoExiste = True  #El código existe en algún cliente
                        break
                if codigoExiste: #Como el código existe, muestra los datos del cliente con dicho código
                    while True:
                        print("\nCLIENTE ENCONTRADO!")
                        print("Código del cliente: \t", cliente_actual["codigoClientes"])#se imprime los datos del cliente encontrado
                        print("Nombre del cliente: \t", cliente_actual["nombreClientes"])
                        print("Cuenta del cliente: \t", cliente_actual["numeroCuentas"])
                        print("\n1.Código\n2.Nombre\n3.Número de cuenta\n0.Salir\n")
                        seleccion = manejoErrorINT("¿Qué desea modificar?: ")#se le da a elegir qué es lo que quiere modificar
                        if seleccion == 0: #por si quiere salir antes de el proceso
                                codigoExiste = False
                                break

                        if seleccion == 1:#si quiere modificar el código del cliente
                            print("\nSi desea cancelar y salir presione 0, seguido de Enter")
                            nuevoCodigo = manejoErrorINT("\tIngrese el nuevo código del cliente: ") #solicito los nuevos datos
                            
                            if nuevoCodigo == 0: #por si quiere salir antes de el proceso
                                codigoExiste = False
                                break

                            codigoExiste = False  
                            for cliente in banco:
                                if cliente["codigoClientes"] == nuevoCodigo : 
                                    codigoExiste = True #aquí se valida, si el nuevo código esta en clientes 
                                    break

                            if nuevoCodigo == codigo:#si el codigo es igual al anterior no modificará nada
                                print("\n   --- No ingrese el codigo anterior del cliente ---")
                                continue
                            
                            if not codigoExiste: #ahora reemplazamos los datos del usuario
                                cliente_actual["codigoClientes"] = nuevoCodigo
                                print("\n   --- El cliente ha sido modificado con éxito! ---")
                                break

                            else:
                                print("\n   --- El código ya lo posee otro cliente ---")
                                continue
                            break
                            
                        elif seleccion == 2: #si quiere cambiar el nombre
                            print("\nSi desea cancelar y salir presione 0, seguido de Enter")
                            nuevoNombre = manejoErrorSTR("\tIngrese el nuevo nombre del Cliente: ")#se le solicita el nuevo nombre 
                            if nuevoNombre == 0: #por si quiere salir antes de el proceso
                                codigoExiste = False
                                break
                            
                            cliente_actual["nombreClientes"] = nuevoNombre #se le reasigna el nombre
                            print("\n   --- El cliente ha sido modificado con éxito! ---")  
                            break

                        elif seleccion == 3:#Si quiere cambiar el numero de cuenta
                            cuentaActual = manejoErrorINT("Ingrese el número de cuenta actual: ")#lo utilizaremos para validar el numero
                            while True:
                                print("\nSi desea cancelar y salir presione 0, seguido de Enter")
                                nuevaCuenta = manejoErrorINT("Ingrese el nuevo número de cuenta: ")#será el nuevo numero de cuenta
                                if nuevaCuenta == 0: #por si quiere salir antes de el proceso
                                    codigoExiste = False
                                    break

                                if nuevaCuenta == cuentaActual: #si el nuevo numero es igual al anterior, no se hará ningún cambio
                                    print("\n   --- No ingrese el numero de la cuenta anterior del cliente ---")
                                    continue

                                cuentaExiste = False
                                for cliente in banco: #aquí se busca si el nuevo numero ya existe en otro cliente
                                    if cliente["numeroCuentas"] == nuevaCuenta:
                                        cuentaExiste = True
                                        break

                                if not cuentaExiste: #una vez validado se asigna el nuevo numero de cuenta
                                    cliente_actual["numeroCuentas"] = nuevaCuenta
                                    print("\n   --- El cliente ha sido modificado con éxito! ---")
                                    break

                                else:#si ya existe el numero de cuenta, imprimirá el mensaje 
                                    print("\n   --- El número de cuenta ya lo posee otro cliente. ---")
                                    continue
                            break

                        if nuevoCodigo == 0: #aquí genera la salida del usuario, cuando este quiera salir
                            codigoExiste = False
                            break
                    break
                else:
                    print("\n    --- Cliente no encontrado! ---")
                    
            break
        else:
            print("   --- No hay clientes ---")

    elif respuesta == 4:
        cargador()
        #Verifica si hay clientes sino hay muestra un mensaje que no hay y lo saca porque sino hay que mas tiene que hacer aqui xd
        if cantClientes > 0:
            print(" --- ELIMINAR CLIENTE --- ")
            while True:
                codigo = manejoErrorINT("\nDigite el código de cliente: ")
                for indice, cliente in enumerate(banco): #le indicamos que numere y que nos dé en la variable indice, la posición del cliente
                    if cliente["codigoClientes"] == codigo:
                        print("\n   --- CLIENTE ENCONTRADO! ---") #mostramos los datos del cliente 
                        print("\nCodigo Cliente: \t", cliente["codigoClientes"])
                        print("Nombre Cliente: \t", cliente["nombreClientes"])
                        print("Cuenta N°: \t\t", cliente["numeroCuentas"])
                        
                        confirmation = input("\n¿DESEA ELIMINAR EL CLIENTE? (si/no): ")
                        if confirmation.lower() == "si":
                            banco.pop(indice) #con esta función lo eliminamos y restamos a la cantidad total de clientes
                            cantClientes -= 1
                            print("\n   --- Se elimino el cliente correctamente ---")
                        elif confirmation.lower() == "no":
                            print("\n   --- No se elimino el cliente ---")
                        
                        else:
                            print("\nHa ingresado una opción incorrecta. Por favor ingresa una opción del submenú.")
                break
        else:
            print("   --- No hay clientes ---")
            
    elif respuesta == 5:  
        cargador()
        if cantClientes > 0:
            print("           --- LISTA DE CLIENTES CON SUS RESPECTIVOS DEPOSITOS --- ") 
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
            print("           --- LISTA DE CLIENTES CON SUS RESPECTIVOS RETIROS --- ") 
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
            print("                                 --- LISTA DE CLIENTES ORDENADA SEGÚN NÚMERO DE CUENTA ---")
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
