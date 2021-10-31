import uuid


class PeluqueriaCanina:
    def __init__(self, nombre, precio=0):
        self.idMascota = uuid.uuid4()
        self.nombre = nombre
        self.precio = precio

    def editar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # def editarCantidad(self, nuevaCantidad):
    #     self.cantidad = nuevaCantidad

    def __repr__(self):
        return "Nombre Mascota: " + self.nombre + " Codigo : " + str(self.idMascota)

    def cumple(self, especificacion):
        dict_mascota = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_mascota or dict_mascota[k] != especificacion.get_value(k):
                return False
        return True
