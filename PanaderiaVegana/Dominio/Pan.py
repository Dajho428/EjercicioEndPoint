import uuid


class Pan:
    def __init__(self, clase, precio=0):
        self.idPan = uuid.uuid4()
        self.clase = clase
        self.precio = precio

    def editarPrecio(self, nuevoPrecio):
        self.precio = nuevoPrecio

    def __repr__(self):
        return "Pan: "+self.clase+" Codigo: " + str(self.idPan)

    def cumple(self, especificacion):
        dict_pan = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_pan or dict_pan[k] != especificacion.get_value(k):
                return False
        return True
