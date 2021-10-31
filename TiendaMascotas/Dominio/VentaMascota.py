import uuid


class VentaMascota:

    def __init__(self, tipo, raza, precio=0):
        self.idVentaMascota = uuid.uuid4()
        self.tipo = tipo
        self.raza = raza
        self.precio = precio
        # self.cantidad = cantidad

    def editar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # def editarCantidad(self, nuevaCantidad):
    #     self.cantidad = nuevaCantidad

    def __repr__(self):
        return "Tipo de mascota: " + self.tipo + " Raza: " + self.raza + " Codigo : " + str(self.idVentaMascota)

    def cumple(self, especificacion):
        dict_venta_mascota = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_venta_mascota or dict_venta_mascota[k] != especificacion.get_value(k):
                return False
        return True
