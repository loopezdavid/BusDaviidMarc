from cliente import Cliente
from bus import Bus
from billete import Billete
def ventaBilletes(plazas_libres, plazas_vendidas, plazas_solicitadas):
    if plazas_solicitadas < plazas_libres:
        plazas_vendidas += plazas_solicitadas
        plazas_libres -= plazas_solicitadas
        return plazas_libres, plazas_vendidas, "Se vendieron " + str(plazas_solicitadas) + " billetes"
    else:
        return plazas_libres, plazas_vendidas,"No hay plazas libres"

def devolucionBilletes(plazas_libres, plazas_vendidas, devolucion):
    if devolucion <= plazas_vendidas:
        plazas_libres += devolucion
        plazas_vendidas -= devolucion
        return plazas_libres, plazas_vendidas, "Se devolvieron " + str(devolucion) + " billetes"
    else:
        return plazas_libres,plazas_vendidas, "Error"

def bus():
    ending = False
    PLAZAS_TOTALES = int(input("Ingrese el número de asientos\n"))
    cliente1 = Cliente("Juan", "Perez")
    cliente2 = Cliente("Pepe", "Garcia")
    cliente3 = Cliente("Lucas", "Santiago")
    bus1 = Bus(1, 50,50)
    bus2 = Bus(2, 30,30)
    bus3 = Bus(3, 20,20)
    plazas_vendidas, plazas_libres = 0, PLAZAS_TOTALES

    print(f"1.- Venta de billetes.\n2.- Devolución de billetes.\n3.- Estado de la venta.\n0.- Salir.")
    while ending == False:
        select = int(input())
        if select == 0: 
            ending = True
        elif select == 1:
            plazas_solicitadas = int(input())
            plazas_libres, plazas_vendidas, mensaje = ventaBilletes(plazas_libres, plazas_vendidas, plazas_solicitadas)
            print(mensaje)
        elif select == 2:
            devolucion = int(input())
            plazas_libres, plazas_vendidas, mensaje = devolucionBilletes( plazas_libres, plazas_vendidas, devolucion)
            print(mensaje)
        elif select == 3:
            print(f"Total: {PLAZAS_TOTALES}\nLibre: {plazas_libres}\nVendido: {plazas_vendidas}")
        else:
            print("Valor incorrecto")  
bus()