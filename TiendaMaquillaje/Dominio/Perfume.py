import uuid


class Perfume:
    def __init__(self, fabricante, nombre, precio=0):
        self.idPerfume = str(uuid.uuid4())
        self.fabricante = fabricante
        self.nombre = nombre
        self.precio = precio
        # self.cantidad = cantidad

    def editar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # def editarCantidad(self, nuevaCantidad):
    #     self.cantidad = nuevaCantidad

    def __repr__(self):
        return "Tipo: " + self.fabricante + " Nombre: " + self.nombre + " Código : " + str(self.idPerfume)

    def cumple(self, especificacion):
        dict_perfume = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_perfume or dict_perfume[k] != especificacion.get_value(k):
                return False
        return True
