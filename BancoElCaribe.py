<<<<<<< HEAD
#Punto 7:

#Uso el diccionario:

clientes = [[numeroCuenta], [codigoCliente], [nombreCliente], [transaccion]]

#Ordeno los clientes según su numero de cuenta:

clientes_ordenados = sorted(clientes, key = lambda x: x[numeroCuenta])

#Muestro la lista ordenada:

for clientes in clientes_ordenados:
    print(f"Numero de cuenta: ", {clientes[numero_Cuenta]})
    print("Código de cuenta: ", {clientes[codigo_Cliente]})
    print("Nombre del Cliente: ",{clientes[nombre_Cliente]})
    print("Trasacción: ", {clientes[transaccion]})


#Punto 8:

#SALIDA DEL PROGRAMA:

print("""\n
           *************************************************************
           *                   BANCO EL CARIBE                         *
           *************************************************************""")



print("\nHa llegado a la última opción de nuestro programa: ")
print("\n8. Salir del programa.")


while True:
    salir = input("\n¿Desea salir del programa? si/no: ")
    if salir.lower() == "si":
        print("\nHa finalizado el programa.")
        print("""
                  *****************************************************
                  *         GRACIAS POR USAR NUESTROS SERVICIOS       *
                  *****************************************************""")
        break
    elif salir.lower() == "no":
        continue
    else:
        print("\nRespuesta inválida. Por favor responda ´si´ o ´no´.")
        continue
=======
print("Hola xd")
print("Mañana no hay clases xdxd")
print("No se que hacer mañana en tutoría xd")
print("holis")
>>>>>>> 2dfaaba1cb3ee3c12333ca81628d590ba6a7b694
