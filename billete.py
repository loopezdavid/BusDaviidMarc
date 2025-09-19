from bus import Bus
from cliente import Cliente

class Billete: 
    def __init__(self, cliente: Cliente, bus: Bus):
       self.cliente = cliente
       self.bus = bus

    def fullBillete (self):
        return f"Billete de {self.cliente.getNombre()} {self.cliente.getApellido()} en el bus {self.bus.getIdBus()}"