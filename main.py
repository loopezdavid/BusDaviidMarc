from cliente import Cliente
from bus import Bus
from billete import Billete
def ventaBilletes(busSelected: Bus):
    if busSelected.getPlazasLibre() > 0:
        busSelected.setPlazasLibre(busSelected.getPlazasLibre() - 1)
        return busSelected
    
def devolucionBilletes(plazas_libres, plazas_vendidas, devolucion):
    if devolucion <= plazas_vendidas:
        plazas_libres += devolucion
        plazas_vendidas -= devolucion
        return plazas_libres, plazas_vendidas, "Se devolvieron " + str(devolucion) + " billetes"
    else:
        return plazas_libres,plazas_vendidas, "Error"

def bus():
    ending = False
    busSelected = 0
    buses = [
        Bus(1, 50,50),
        Bus(2, 30,30),
        Bus(3, 20,20)
    ]
    billetes = []

    print(f"1.- Venta de billetes.\n2.- Devolución de billetes.\n3.- Estado de la venta.\n0.- Salir.")
    while ending == False:
        select = int(input())
        if select == 0: 
            ending = True
        elif select == 1:
            nombre = input("Ingrese su nombre\n")
            apellido = input("Ingrese su apellido\n") 
            for bus in buses:
                print(f"Elige Bus entre: {bus.getIdBus()}")
            busSelected=int(input())
            billetes.append(Billete(Cliente(nombre, apellido), ventaBilletes(buses[busSelected-1])))
            for billete in billetes:
                print(billete.fullBillete())
        # elif select == 2:1
        #     devolucion = int(input())
        #     plazas_libres, plazas_vendidas, mensaje = devolucionBilletes( plazas_libres, plazas_vendidas, devolucion)
        #     print(mensaje)
        # elif select == 3:
        #     print(f"Total: {}\nLibre: {plazas_libres}\nVendido: {plazas_vendidas}")
        else:
            print("Valor incorrecto")  
bus()