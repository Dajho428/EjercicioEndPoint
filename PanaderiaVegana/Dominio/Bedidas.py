import uuid


class Bebida:
    def __init__(self, nombreBebida,  precio=0):
        self.idBebida = uuid.uuid4()
        self.nombreBebida = nombreBebida
        self.precio = precio
        # self.cantidad = cantidad

    def editarPrecio(self, nuevoPrecio):
        self.precio = nuevoPrecio

    # def editarCantidad(self, nuevaCantidad):
    #     self.cantidad = nuevaCantidad

    def __repr__(self):
        return "Bebida: "+self.nombreBebida+" Codigo : " + str(self.idBebida)

    def cumple(self, especificacion):
        dict_bebida = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_bebida or dict_bebida[k] != especificacion.get_value(k):
                return False
        return True
