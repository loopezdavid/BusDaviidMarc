class Bus:
    def __init__(self, idBus, plazasLibre, plazasTotales):
        self.idBus = idBus
        self.plazasLibre = plazasLibre
        self.plazasTotales = plazasTotales

    def getIdBus(self):
        return self.idBus
    def getPlazasLibre(self):
        return self.plazasLibre
    def getPlazasTotales(self):     
        return self.plazasTotales       
    def setIdBus(self, idBus):
        self.idBus = idBus  
    def setPlazasLibre(self, plazasLibre):
        self.plazasLibre = plazasLibre           
    def setPlazasTotales(self, plazasTotales):
        self.plazasTotales = plazasTotales  