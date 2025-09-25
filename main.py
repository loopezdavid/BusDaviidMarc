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

def validationId(idBus, buses):
    for i in buses: 
        if i.getIdBus() == idBus:
            return False
    return True
def nombreValido(nombre):
    if nombre.strip() == "" or len(nombre) < 3 or len(nombre) > 30 :
        return False
    return True

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
        print(f"1.- Venta de billetes.\n2.- Devolución de billetes.\n3.- Estado de la venta.\n4.- Añadir Bus\n5.- Ver buses\n0.- Salir.")
        select = input()
        if not select.isdigit():
            print("Ha de ser un numero ")
            continue
        select = int(select)
        if select == 0: 
            ending = True
        elif select == 1:
            nombre = input("Ingrese su nombre\n")
            if not nombreValido(nombre):
                print("Nombre no válido")
                continue
            apellido = input("Ingrese su apellido\n") 
            if not nombreValido(apellido):
                print("Apellido no válido")
                continue
            for bus in buses:
                print(f"Bus : {bus.getIdBus()} || Plazas libres: {bus.getPlazasLibre()}")
            busSelected=int(input())
            if busSelected < 1 or busSelected > len(buses):
                print("Bus no existente")
                continue
            clientes.append(Cliente(nombre, apellido))
            billetes.append(Billete(Cliente(nombre.strip(), apellido.strip()), ventaBilletes(buses[busSelected-1])))
            for billete in billetes:
                print(billete.fullBillete())
        elif select == 2:
            print("Quien eres?")
            for i in clientes: 
                print(f" {i.getNombre()} {i.getApellido()}")
            nombre = input().strip()
            apellido = input().strip()
            for billete in billetes:
                if (billete.cliente.getNombre().lower() == nombre.lower() and
                    billete.cliente.getApellido().lower() == apellido.lower()):
                    devolucionBilletes(billete)       
                    billetes.remove(billete)
                    for i in clientes: 
                        if i.getNombre().lower() == nombre.lower() and i.getApellido().lower() == apellido.lower():
                            clientes.remove(i)
                    for billete in billetes: 
                        print(billete.fullBillete())
                else : 
                    print("No tienes billete")
                     # plazas_libres, plazas_vendidas, mensaje = devolucionBilletes( plazas_libres, plazas_vendidas, devolucion)
        elif select == 3:
            for billete in billetes: 
                print(billete.fullBillete())
                     # plazas_libres, plazas_vendidas, mensaje = devolucionBilletes( plazas_libres, plazas_vendidas, devolucion)
        elif select == 4:
            idBus = int(input("Ingrese el ID del bus\n"))
            validation = validationId(idBus, buses)
            if validation:
                plazas = int(input("Ingrese el número de plazas del bus\n"))
                if plazas < 1 or plazas > 100: 
                    print("Número de plazas no válido")
                else :
                    buses.append(Bus(idBus, plazas, plazas))
                    print("Bus creado")
            else:
                print("El ID del bus ya existe")
        elif select == 5:
            for bus in buses:
                print(bus.fullBus())
        
        else:
            print("Valor incorrecto")
 
bus()
