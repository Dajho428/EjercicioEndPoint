import uuid


class Maquillaje:
    def __init__(self, tipo, nombre, precio=0):
        self.idMaquillaje = uuid.uuid4()
        self.tipo = tipo
        self.nombre = nombre
        self.precio = precio
        # self.cantidad = cantidad

    def editar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # def editarCantidad(self, nuevaCantidad):
    #     self.cantidad = nuevaCantidad

    def __repr__(self):
        return "Tipo: " + self.tipo + " Nombre: " + self.nombre + " Codigo : " + str(self.idMaquillaje)

    def cumple(self, especificacion):
        dict_maquillaje = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_maquillaje or dict_maquillaje[k] != especificacion.get_value(k):
                return False
        return True
