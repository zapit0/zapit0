import os
opcion = ""
cestrellam = 0
champs = 0
meganium = 0
donkie = 0
totalVentas = 0
fueVendida = False
descuento = 10
while opcion != "5":
    os.system("cls")
    print("******** heladeria fan`s levi live ********")
    print("1.- Cestrellan $500")
    print("2.- Champs $4000")
    print("3.- Meganium $2500")
    print("4.- Donkie $2000")
    print("5.- Salir")
    opcion = input("Ingrese una opción:")
    if opcion not in ("1", "2", "3", "4", "5", ):
        print("La opción no es válida")
    elif opcion == "5":
        print("**** REPORTE ****")
        print(f"cestrellam: {cestrellam}")
        print(f"champs: {champs}")
        print(f"meganium: {meganium}")
        print(f"donkie: {donkie}")
        print(f"total de ventas: ${int(totalVentas)}")
        print("Total de helados:", ( cestrellam + champs + meganium + donkie))
    elif opcion == "1":
        totalVentas = totalVentas + 500
        cestrellam += 1
        edad = int(input("ingrese su edad:"))
        if edad < 18 or edad > 65:
            if edad < 18 or edad > 65:
                print("usted tiene un descuento del 10%")
                totalVentas = totalVentas - (descuento * 500 / 100)
    if opcion == "2":
        totalVentas = totalVentas + 4000
        champs += 1
        edad = int(input("ingrese su edad:"))
        if edad < 18 or edad > 65:
            if edad < 18 or edad > 65:
                print("usted tiene un descuento del 10%")
                totalVentas =  (descuento * 4000 / 100)
    elif opcion == "3":       
        totalVentas = totalVentas + 2500
        meganium += 1
        edad = int(input("ingrese su edad:"))
        if edad < 18 or edad > 65:
            if edad < 18 or edad > 65 :
                print("usted tiene un descuento del 10%")
                totalVentas = totalVentas - (descuento * 2500 / 100)
    elif opcion == "4":        
        totalVentas = totalVentas + 2000
        donkie += 1
        edad = int(input("ingrese su edad:"))
        if edad < 18 or edad > 65:
            if edad < 18 or edad > 65:
                print("usted tiene un descuento del 10%")
                totalVentas = totalVentas - (descuento * 2000 / 100)
    input("Presione enter para continuar")