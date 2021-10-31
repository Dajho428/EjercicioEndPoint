import uuid


class Esmalte:
    def __init__(self, marca, color, precio=0):
        self.idEsmalte = uuid.uuid4()
        self.marca = marca
        self.color = color
        self.precio = precio
        # self.cantidad = cantidad

    def editar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # def editarCantidad(self, nuevaCantidad):
    #     self.cantidad = nuevaCantidad

    def __repr__(self):
        return "Marca: " + self.marca + " Color: " + self.color + " Código : " + str(self.idEsmalte)

    def cumple(self, especificacion):
        dict_esmalte = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_esmalte or dict_esmalte[k] != especificacion.get_value(k):
                return False
        return True
