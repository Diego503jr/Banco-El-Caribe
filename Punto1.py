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

while True:
    resp = int(input("1, 2 o 3?: "))
    if resp == 1: 
        cant = int(input("¿Cuántos clientes agregará?: "))
        for i in range(cant):
            print("Cliente N°", cantClientes+1)
            codigoClientes = input("Digite el código del cliente: ")
            nombreClientes = input("Digite el nombre del cliente: ")
            numeroCuenta = input("Digite el numero de cuenta: ")
            clientes["codigoClientes"].append(codigoClientes)
            clientes["nombreClientes"].append(nombreClientes)
            clientes["numeroCuenta"].append(numeroCuenta)
            cantClientes += 1
    elif resp == 2:
        codigo = input("Digite el código de cliente: ")
        for i in range(cantClientes):
            if(clientes["codigoClientes"][i] == codigo):
                print("Cliente encontrado!")
                print("Codigo de Clientes: ", clientes["codigoClientes"][i])
                print("Nombre: ", clientes["nombreClientes"][i])
                print("Cuenta N°: ", clientes["numeroCuenta"][i])
                print()
                tipoTransaccion = int(input("Qué tipo de transacción hará:\n1. Depósito\n2. Retiro\n"))
                if tipoTransaccion == 1:
                    valorDeposito = float(input("Digite la cantidad a depositar: $"))
                    totDep += valorDeposito
                    fecha = input("Digite la fecha de este depósito: ")
                    clientes["depositos"[i]].append(valorDeposito)
                    clientes["fecha"[i]].append(fecha)
                elif tipoTransaccion == 2:
                    valorRetiro = float(input("Digite la cantidad a retirar: $"))
                    totRet += valorRetiro
                    fecha = input("Digite la fecha de este retiro: ")
                    clientes["retiros"[i]].append(valorRetiro)
                    clientes["fecha"[i]].append(fecha)
                else:
                    print("Opción inválida")
        saldoF = totDep - totRet
    elif resp == 3:
        for i in range(cantClientes):
            print(clientes["codigoClientes"][i])
            print(clientes["nombreClientes"][i])
            print(clientes["numeroCuenta"][i])
            print(clientes["depositos"][i])
            print(clientes["retiros"][i])
            print(clientes["fecha"][i],"\n")
        print("Total: $", totDep)
        print("Total: ", totRet)
        print("Saldo Final", saldoF)
    elif resp == 8:
        break
    else:
        print("Opción invalida")