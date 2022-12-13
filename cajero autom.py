#Cajero automatico en consola
saldocaj= 10000 #saldo de caja 

#----------Datos de usuarios------------

#Usuario 1
saldo1= 5000 
numcuenta1= 10203040
contraseña1= 1234

#Uusario 2
saldo2=2500
numcuenta2= 11223344
contraseña2= 4321

#Usuario 3
saldo3= 3000
numcuenta3= 66778899
contraseña3= 6789
#----------------------------------------

def menu_operaciones(print):
  print(""" 
•───────────────────────────────•
|    MENU DE OPERACIONES        |
|    Operaciones a relizar      |
|    1: Consultar saldo         |
|    2: Depositar               |
|    3: Retirar                 | 
|    4: Cambiar PIN             |
|    5: Salir                   |
•───────────────────────────────• """)
  return

def menu_depositos(print):
  print(""" 
→→→→→→→→→→→→→→→→→→→→→→→→→→→
|    MENU DE DEPOSITOS    |
|    1: Depostiar $100    |
|    2: Depositar $200    |
|    3: Depositar $500    |
|    4: Depositar $1000   |
|    5: Depositar $2000   |
|    6: Otra cantidad     |
|    7: Salir             |
→→→→→→→→→→→→→→→→→→→→→→→→→→→""")
  return

def menu_retiros(print):
  print(""" 
←←←←←←←←←←←←←←←←←←←←←←←
|  MENU DE RETIROS    |
|  1: Retirar $100    |
|  2: Retirar $200    |
|  3: Retirar $500    |
|  4: Retirar $1000   |
|  5: Retirar $2000   |
|  6: Otra cantidad   |
|  7: Salir           |
←←←←←←←←←←←←←←←←←←←←←←←""")
  return

print("""
            ┏━━━━━❂❂━━━━━━━━━━❂❂━━━━━┓
                Cajero automatico  
            ┗━━━━━❂❂━━━━━━━━━━❂❂━━━━━┛""")
while True:
    print('')
    print("Saldo actual del cajero: " ,saldocaj)
    usuario= input("Ingrese su nombre: ")
    print('')
    print("             Bienvenido(a) " ,usuario )
    print('')
    cuenta=int(input("Escriba su número de cuenta: "))
    if cuenta == numcuenta1:
        while True:
            c= int(input("Escriba su contraseña: "))
            if c== contraseña1:
                print("Saldo actual del cajero: " ,saldocaj)
                while True:
                    menu_operaciones(print)
                    o=int(input("Seleccione un numero: "))
                    #OPCION 1 CONSULTA DE SALDO
                    if o == 1: 
                        print('')
                        print(" *** Usuario: " ,usuario)
                        print(" *** Número de cuenta: " ,cuenta)
                        print(" *** Saldo actual $" ,saldo1)
                    if o == 2:
                        menu_depositos(print)
                        depo=int(input("Seleccione opcion de deposito: "))
                        if depo == 1:
                            print('')
                            print('Selecciono un deposito de $100')
                            print('Se ha depositado exitosamente, le sujerimos consultar su saldo')
                            saldo1= saldo1 + 100
                        elif depo == 2:
                            print('')
                            print('Selecciono un deposito de $200')
                            print('Se ha depositado exitosamente, le sujerimos consultar su saldo')
                            saldo1= saldo1 + 200
                        elif depo == 3:
                            print('')
                            print('Selecciono un deposito de $500')
                            print('Se ha depositado exitosamente, le sujerimos consultar su saldo')
                            saldo1= saldo1 + 500
                        elif depo == 4:
                            print('')
                            print('Selecciono un deposito de $1000')
                            print('Se ha depositado exitosamente, le sujerimos consultar su saldo')
                            saldo1= saldo1 + 1000
                        elif depo == 5:
                            print('')
                            print('Selecciono un deposito de $2000')
                            print('Se ha depositado exitosamente, le sujerimos consultar su saldo')
                            saldo1= saldo1 + 2000
                        elif depo == 6:
                            print('')
                            print('Selecciono un deposito independiente')
                            depocan= int(input("Ingrese la cantidad de deposito: ")) #Otra opcion de deposito
                            saldo1= saldo1 + depocan
                            print('Se ha depositado exitosamente, le sujerimos consultar su saldo')
                        elif depo == 7:
                          break
                        else:
                            print('')
                            print("Opcion incorrecta")
                            break
                    if o == 3:
                        menu_retiros(print)
                        retiro =int(input("Seleccione una cantidad de retiro: "))
                        if retiro == 1:
                            saldo1= saldo1 - 100
                            saldocaj= saldocaj - 100
                            print('')
                            print('Su retiro fue exitoso, le sujerimos consultar su saldo')
                        elif retiro == 2:
                            saldo1= saldo1 - 200
                            saldocaj= saldocaj - 200
                            print('')
                            print('Su retiro fue exitoso, le sujerimos consultar su saldo')
                        elif retiro == 3:
                            saldo1= saldo1 - 500
                            saldocaj= saldocaj -500
                            print('')
                            print('Su retiro fue exitoso, le sujerimos consultar su saldo')
                        elif retiro == 4:
                            saldo1= saldo1 - 1000
                            saldocaj= saldocaj - 1000
                            print('')
                            print('Su retiro fue exitoso, le sujerimos consultar su saldo')
                        elif retiro == 5:
                            saldo1= saldo1 -2000
                            saldocaj= saldo1 -2000
                            print('')
                            print('Su retiro fue exitoso, le sujerimos consultar su saldo')
                        elif retiro == 6:
                            recan= int(input("Ingrese la cantidad a retirar: ")) #otra opción de retiro
                            if recan < saldocaj:
                                if recan <saldo1:  
                                    saldo1= saldo1 - recan
                                    saldocaj= saldocaj - recan
                                    print('')
                                    print('Su retiro fue un exito, le sujerimos consultar su saldo')                     
                                else:
                                    print('')
                                    print('Lo sentimos no  cuenta con fondos suficientes')
                            else:
                                print('')
                                print('Lo sentimos el cajero no cuenta con fondos suficientes')
                    if o == 4:
                        print('')
                        pin= int(input("Ingrese su nueva contraseña: "))
                        contraseña1= pin
                    elif o == 5:
                        print('''
===============================================
    Gracias por su elección, vuelva pronto 
=============================================== ''')
                        break
                break                 
            else: 
              print("Contraseña incorrecta")

    elif cuenta == numcuenta2:
        while True:
            c= int(input("Escriba su contraseña: "))
            if c== contraseña2:
                print("Saldo actual del cajero: " ,saldocaj)
                while True:
                    menu_operaciones(print)
                    o=int(input("Seleccione un numero: "))
                    #OPCION 1 CONSULTA DE SALDO
                    if o == 1: 
                        print('')
                        print(" *** Usuario: " ,usuario)
                        print(" *** Número de cuenta: " ,cuenta)
                        print(" *** Saldo actual $" ,saldo2)
                    if o == 2:
                        menu_depositos(print)
                        depo=int(input("Seleccione opcion de deposito: "))
                        if depo == 1:
                            print('')
                            print('Selecciono un deposito de $100')
                            print('Se ha depositado exitosamente, le sujerimos consultar su saldo')
                            saldo2= saldo2 + 100
                        elif depo == 2:
                            print('')
                            print('Selecciono un deposito de $200')
                            print('Se ha depositado exitosamente, le sujerimos consultar su saldo')
                            saldo2= saldo2 + 200
                        elif depo == 3:
                            print('')
                            print('Selecciono un deposito de $500')
                            print('Se ha depositado exitosamente, le sujerimos consultar su saldo')
                            saldo2= saldo2 + 500
                        elif depo == 4:
                            print('')
                            print('Selecciono un deposito de $1000')
                            print('Se ha depositado exitosamente, le sujerimos consultar su saldo')
                            saldo2= saldo2 + 1000
                        elif depo == 5:
                            print('')
                            print('Selecciono un deposito de $2000')
                            print('Se ha depositado exitosamente, le sujerimos consultar su saldo')
                            saldo2= saldo2 + 2000
                        elif depo == 6:
                            print('')
                            print('Selecciono un deposito independiente')
                            depocan= int(input("Ingrese la cantidad de deposito: ")) #Otra opcion de deposito
                            saldo2= saldo2 + depocan
                            print('Se ha depositado exitosamente, le sujerimos consultar su saldo')
                        elif depo == 7:
                          break
                        else:
                            print('')
                            print("Opcion incorrecta")
                            break
                    if o == 3:
                        menu_retiros(print)
                        retiro =int(input("Seleccione una cantidad de retiro: "))
                        if retiro == 1:
                            saldo2= saldo2 - 100
                            saldocaj= saldocaj - 100
                            print('')
                            print('Su retiro fue exitoso, le sujerimos consultar su saldo')
                        elif retiro == 2:
                            saldo2= saldo2 - 200
                            saldocaj= saldocaj - 200
                            print('')
                            print('Su retiro fue exitoso, le sujerimos consultar su saldo')
                        elif retiro == 3:
                            saldo2= saldo2 - 500
                            saldocaj= saldocaj -500
                            print('')
                            print('Su retiro fue exitoso, le sujerimos consultar su saldo')
                        elif retiro == 4:
                            saldo2= saldo2 - 1000
                            saldocaj= saldocaj - 1000
                            print('')
                            print('Su retiro fue exitoso, le sujerimos consultar su saldo')
                        elif retiro == 5:
                            saldo2= saldo2 -2000
                            saldocaj= saldo1 -2000
                            print('')
                            print('Su retiro fue exitoso, le sujerimos consultar su saldo')
                        elif retiro == 6:
                            recan= int(input("Ingrese la cantidad a retirar: ")) #otra opción de retiro
                            if recan < saldocaj:
                                if recan <saldo2:  
                                    saldo2= saldo2 - recan
                                    saldocaj= saldocaj - recan
                                    print('')
                                    print('Su retiro fue un exito, le sujerimos consultar su saldo')                     
                                else:
                                    print('')
                                    print('Lo sentimos no  cuenta con fondos suficientes')
                            else:
                                print('')
                                print('Lo sentimos el cajero no cuenta con fondos suficientes')
                    if o == 4:
                        print('')
                        pin= int(input("Ingrese su nueva contraseña: "))
                        contraseña2= pin
                    elif o == 5:
                        print('''
===============================================
    Gracias por su elección, vuelva pronto 
=============================================== ''')
                        break
                break                 
            else: 
              print("Contraseña incorrecta")

    elif cuenta == numcuenta3:
        while True:
            c= int(input("Escriba su contraseña: "))
            if c== contraseña3:
                print("Saldo actual del cajero: " ,saldocaj)
                while True:
                    menu_operaciones(print)
                    o=int(input("Seleccione el numero de una operacion: "))
                    #OPCION 1 CONSULTA DE SALDO
                    if o == 1: 
                        print('')
                        print(" *** Usuario: " ,usuario)
                        print(" *** Número de cuenta: " ,cuenta)
                        print(" *** Saldo actual $" ,saldo3)
                    if o == 2:
                        menu_depositos(print)
                        depo=int(input("Seleccione opcion de deposito: "))
                        if depo == 1:
                            print('')
                            print('Selecciono un deposito de $100')
                            print('Se ha depositado exitosamente, le sujerimos consultar su saldo')
                            saldo3= saldo3 + 100
                        elif depo == 2:
                            print('')
                            print('Selecciono un deposito de $200')
                            print('Se ha depositado exitosamente, le sujerimos consultar su saldo')
                            saldo3= saldo3 + 200
                        elif depo == 3:
                            print('Selecciono un deposito de $500')
                            print('Se ha depositado exitosamente, le sujerimos consultar su saldo')
                            saldo3= saldo3 + 500
                        elif depo == 4:
                            print('')
                            print('Selecciono un deposito de $1000')
                            print('Se ha depositado exitosamente, le sujerimos consultar su saldo')
                            saldo3= saldo3 + 1000
                        elif depo == 5:
                            print('')
                            print('Selecciono un deposito de $2000')
                            print('Se ha depositado exitosamente, le sujerimos consultar su saldo')
                            saldo3= saldo3 + 2000
                        elif depo == 6:
                            print('')
                            print('Selecciono un deposito independiente')
                            depocan= int(input("Ingrese la cantidad de deposito: ")) #Otra opcion de deposito
                            saldo3= saldo3 + depocan
                            print('Se ha depositado exitosamente, le sujerimos consultar su saldo')
                        elif depo == 7:
                          break
                        else:
                            print('')
                            print("Opcion incorrecta")
                            break
                    if o == 3:
                        menu_retiros(print)
                        retiro =int(input("Seleccione una cantidad de retiro: "))
                        if retiro == 1:
                            saldo3= saldo3 - 100
                            saldocaj= saldocaj - 100
                            print('')
                            print('Su retiro fue exitoso, le sujerimos consultar su saldo')
                        elif retiro == 2:
                            saldo3= saldo3 - 200
                            saldocaj= saldocaj - 200
                            print('')
                            print('Su retiro fue exitoso, le sujerimos consultar su saldo')
                        elif retiro == 3:
                            saldo3= saldo3 - 500
                            saldocaj= saldocaj -500
                            print('')
                            print('Su retiro fue exitoso, le sujerimos consultar su saldo')
                        elif retiro == 4:
                            saldo3= saldo3 - 1000
                            saldocaj= saldocaj - 1000
                            print('')
                            print('Su retiro fue exitoso, le sujerimos consultar su saldo')
                        elif retiro == 5:
                            saldo3= saldo3 -2000
                            saldocaj= saldo1 -2000
                            print('')
                            print('Su retiro fue exitoso, le sujerimos consultar su saldo')
                        elif retiro == 6:
                            recan= int(input("Ingrese la cantidad a retirar: ")) #otra opción de retiro
                            if recan < saldocaj:
                                if recan <saldo3:  
                                    saldo3= saldo3 - recan
                                    saldocaj= saldocaj - recan
                                    print('')
                                    print('Su retiro fue un exito, le sujerimos consultar su saldo')                     
                                else:
                                    print('')
                                    print('Lo sentimos no  cuenta con fondos suficientes')
                            else:
                                print('')
                                print('Lo sentimos el cajero no cuenta con fondos suficientes')
                    if o == 4:
                        print('')
                        pin= int(input("Ingrese su nueva contraseña: "))
                        contraseña3= pin
                    elif o == 5:
                        print('''
===============================================
    Gracias por su elección, vuelva pronto 
=============================================== ''')
                        break
                break                 
            else: 
              print("Contraseña incorrecta")
    else:
        print('Usuario no registrado')