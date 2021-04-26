'''
    El aplicativo pretende servir para
    calcular tasa implícita en un préstamo sintético
'''
import os

from datetime import datetime

def menuSintetico():
    os.system('Clear')
    print('Préstamo Sintético')
    print('INGRESE')
    print('\t1 Información Sintético')
    print('\t2 Cálculo Sintético')
    print()

while True:
    menuSintetico()

    opcionMenu = input("Insertar opción: ")

    if opcionMenu=="1":
    #Explicación
        print("Es una herramienta financiera por la que")
        print("se toma un préstamo en moneda local")
        print("por importe equivalente a los USD necesitados")
        print("al tipo de cambio SPOT,")
        print("cuyo destino será aplicarlos, en simultáneo,")
        print("a la venta de dolar futuro a igual plazo que el préstamo,")
        print("y por importe equivalente a capital + intereses.")
        print("La operación compensa por diferencias de tipo de cambio:")
        print("Futuro vendido VS Com. BCRA 3500 de la fecha de vencimiento.")
        print("")
        #regresar: = input("Presione cualquier tecla + Enter para volver al menú principal")
        #   if regresar True:
        #        menu()

    elif opcionMenu=='2':
        #Prestamo en pesos
        capitalEnPesos = float(input("Ingrese el capital del préstamo en pesos: "))

        tasaPrestamo = float(input("Ingrese la tasa. Use '.' para decimales: "))
        tasaPrestamo = tasaPrestamo / 100

        plazoPrestamoPesos = int(input("Ingrese el plazo del préstamo en dias: "))
        plazoPrestamoPesos1 = plazoPrestamoPesos / 365

        intereses = (capitalEnPesos * tasaPrestamo * plazoPrestamoPesos1)

        montoPesos = capitalEnPesos + intereses

        #Spot
        importeFWD = capitalEnPesos
        cambioSpot = float(input("Ingrese Spot use '.' para decimales: "))
        montoSpot = importeFWD // cambioSpot

        #Venta NDF
        cambioNDF = float(input ("Ingrese costo del Futuro use '.' para decimales: "))
        implicitaNDF = (((cambioNDF / cambioSpot) -1) * (365/plazoPrestamoPesos))*100
        montoEnUSD = montoPesos // cambioNDF
        intImplicitos = montoEnUSD - montoSpot

        #Tasa implicita
        tImplicita = ((intImplicitos / montoSpot) * (365/plazoPrestamoPesos))*100

        fechaActual = datetime.now()
        print("")
        print(f'Cotización al {fechaActual}')
        print("")
        print("------Préstamo en pesos------ ")
        print("")
        print('Capital del préstamo:', capitalEnPesos)
        print(f'Plazo del prestamo {plazoPrestamoPesos} días')
        print(f'Intereses del préstamo en pesos: {intereses:.2f}')
        print("")
        print("------Spot------ ")
        print("")
        print('Tipo de cambio SPOT:', cambioSpot)
        print('Préstamo en USD al SPOT:', montoSpot)
        print("")
        print('------Cliente vende DOLAR FUTURO - NDF------')
        print("")
        print(f'Monto a cancelar en pesos: {montoPesos:.2f}')
        print(f'Tipo de cambio NDF: {cambioNDF:.2f}')
        print(f'Tasa implicita NDF: {implicitaNDF:.2f} %')
        print(f'Monto en USD: {montoEnUSD:.2f}')
        print(f'Intereses implicitos:  {intImplicitos:.2f}')
        print("")
        print(f'Tasa implicita:  {tImplicita:.2f} %')

    else:
        print('Opción inexistente. Ingrese una opción válida')
