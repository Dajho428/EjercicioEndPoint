import uuid
from subprocess import call


class Postre:
    def __init__(self, nombrePostre, precio=0):
        self.idPostre = uuid.uuid4()
        self.nombrePostre = nombrePostre
        self.precio = precio

    def editarPrecio(self, nuevoPrecio):
        self.precio = nuevoPrecio

    def __repr__(self):
        return "Postre: "+self.nombrePostre+" Codigo: " + str(self.idPostre)

    def cumple(self, especificacion):
        dict_postre = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_postre or dict_postre[k] != especificacion.get_value(k):
                return False
        return True
