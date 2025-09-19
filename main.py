from cliente import Cliente
from bus import Bus
from billete import Billete
def ventaBilletes(busSelected: Bus):
    if busSelected.getPlazasLibre() > 0:
        busSelected.setPlazasLibre(busSelected.getPlazasLibre() - 1)
        return busSelected
    
def devolucionBilletes(billete: Billete):
    billete.bus.setPlazasLibre(billete.bus.getPlazasLibre() + 1)
    print(f"Billete de: {billete.cliente.getNombre()} {billete.cliente.getApellido()} devuelto")

def bus():
    ending = False
    busSelected = 0
    buses = [
        Bus(1, 50,50),
        Bus(2, 30,30),
        Bus(3, 20,20)
    ]
    clientes:Cliente = []
    billetes = []

    while ending == False:
        print(f"1.- Venta de billetes.\n2.- Devolución de billetes.\n3.- Estado de la venta.\n0.- Salir.")
        select = int(input())
        if select == 0: 
            ending = True
        elif select == 1:
            nombre = input("Ingrese su nombre\n")
            apellido = input("Ingrese su apellido\n") 
            for bus in buses:
                print(f"Bus : {bus.getIdBus()} . Plazas libres: {bus.getPlazasLibre()}")
            busSelected=int(input())
            if busSelected < 1 or busSelected > len(buses):
                print("Bus no existente")
                continue
            clientes.append(Cliente(nombre, apellido))
            billetes.append(Billete(Cliente(nombre.strip(), apellido.strip()), ventaBilletes(buses[busSelected-1])))
            for billete in billetes:
                print(billete.fullBillete())
        elif select == 2:
            for i in clientes: 
                print(f"Quien eres? {i.getNombre()} {i.getApellido()}")
            nombre = input("Nombre: ").strip()
            apellido = input("Apellido: ").strip()
            encontrado = False
            for billete in billetes:
                if (billete.cliente.getNombre().lower() == nombre.lower() and
                    billete.cliente.getApellido().lower() == apellido.lower()):
                    devolucionBilletes(billete)       
                    billetes.remove(billete)
                    encontrado = True
                    break
            if not encontrado:
                print("No se encontró un billete con ese nombre y apellido.")
            for billete in billetes: 
                print(billete.fullBillete())
                     # plazas_libres, plazas_vendidas, mensaje = devolucionBilletes( plazas_libres, plazas_vendidas, devolucion)
        elif select == 3:
            for billete in billetes: 
                print(billete.fullBillete())
                     # plazas_libres, plazas_vendidas, mensaje = devolucionBilletes( plazas_libres, plazas_vendidas, devolucion)
        else:
            print("Valor incorrecto")  
bus()