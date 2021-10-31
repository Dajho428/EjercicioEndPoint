import uuid


class Cosmetico:
    def __init__(self, tipo, nombre, precio=0):
        self.idCosmetico = uuid.uuid4()
        self.tipo = tipo
        self.nombre = nombre
        self.precio = precio
        # self.cantidad = cantidad

    def editar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # def editarCantidad(self, nuevaCantidad):
    #     self.cantidad = nuevaCantidad

    def __repr__(self):
        return "Tipo: " + self.tipo + " Nombre: " + self.nombre + " Codigo : " + str(self.idCosmetico)

    def cumple(self, especificacion):
        dict_cosmetico = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_cosmetico or dict_cosmetico[k] != especificacion.get_value(k):
                return False
        return True

