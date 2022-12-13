#Autor Anett de Jesus Jaramillo Pelayo
saldocaj= 100000
saldo= 25000  ##Usuario 1
numcuenta= 10203040
contraseña= 1234
print("""┏━━━━━❂❂━━━━━━━━━━❂❂━━━━━┓
     Cajero automatico  
┗━━━━━❂❂━━━━━━━━━━❂❂━━━━━┛""")
while True:
    print("Saldo actual del cajero: " ,saldocaj)
    usuario= input("Ingrese su nombre: ")
    print("Bienvenido(a) " ,usuario)
    cuenta=int(input("Escriba su número de cuenta: "))
    if cuenta == 10203040:
        while True:
            c= int(input("Escriba su contraseña: "))
            if c== contraseña:
                print("Saldo actual del cajero: " ,saldocaj)
                while True:
                    print(""" 
    •────────────────────────────────────•
            MENU DE OPERACIONES
        Operaciones a relizar 
        1: Consultar saldo
        2: Depositar
        3: Retirar
        4: Cambiar PIN
        5: Salir
    •────────────────────────────────────• """)
                    o=int(input("Seleccione una opción de las mencionadas anteriormente: "))
                    if o == 1: #Opcion 1 Saldo actual
                        print(" *** Número de cuenta: " ,cuenta)
                        print(" *** Saldo actual $" ,saldo)
                    elif o == 2: #Opcion 2 Depositos
                        print(""" 
        →→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→
                 MENU DE DEPOSITOS
                1: Depostiar $100
                2: Depositar $200
                3: Depositar $500
                4: Depositar $1000
                5: Depositar $2000
                6: Otra cantidad
                7: Salir
        →→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→""")
                        depo=int(input("Seleccione una cantidad a depositar: "))#Variable deposito
                        if depo == 1:
                            saldo= saldo + 100
                        elif depo == 2:
                            saldo= saldo + 200
                        elif depo == 3:
                            saldo= saldo + 500
                        elif depo == 4:
                            saldo= saldo + 1000
                        elif depo == 5:
                            saldo= saldo + 2000
                        elif depo == 6:
                            depocan= int(input("Ingrese la cantidad de deposito: ")) #Otra opcion de deposito
                            saldo= saldo + depocan
                        elif depo == 7:
                            break
                        else:
                            print("Opcion incorrecta")
                            break
                    elif o == 3: #Opcion 3, Retiros
                        print(""" 
            ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
                      MENU DE RETIROS
                   1: Retirar $100
                   2: Retirar $200
                   3: Retirar $500
                   4: Retirar $1000
                   5: Retirar $2000
                   6: Otra cantidad
                   7: Salir
            ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←""")
                        retiro =int(input("Seleccione una cantidad de retiro: "))
                        if retiro == 1:
                            saldo= saldo - 100
                            saldocaj= saldocaj - 100
                        elif retiro == 2:
                            saldo= saldo - 200
                            saldocaj= saldocaj - 200
                        elif retiro == 3:
                            saldo= saldo - 500
                            saldocaj= saldocaj -500
                        elif retiro == 4:
                            saldo= saldo - 1000
                            saldocaj= saldocaj - 1000
                        elif retiro == 5:
                            saldo= saldo -2000
                            saldocaj= saldo -2000
                        elif retiro == 6:
                            recan= int(input("Ingrese la cantidad a retirar: ")) #otra opción de retiro
                            saldo= saldo - recan
                            saldocaj= saldocaj - recan
                        elif retiro == 7:
                            break #Hasta aqui termina la opción 3
                        else:
                            print("Opcion incorrecta")
                            break
                    elif o == 4:#Opción 4 Cambio de contraseña
                        pin= int(input("Ingrese su nueva contraseña: "))
                        contraseña= pin
                        break
                    elif o == 5:
                        print("Gracias por su elección, vuelva pronto ")
                        break
                break          
            else: 
                print("Contraseña incorrecta")            
    else: 
        print("Usuario incorrecto")