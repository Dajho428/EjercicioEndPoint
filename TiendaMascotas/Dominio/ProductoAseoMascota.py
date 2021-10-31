import uuid


class ProductoAseoMascota:
    def __init__(self, tipo, nombre, precio=0):
        self.idProducto = uuid.uuid4()
        self.tipo = tipo
        self.nombre = nombre
        self.precio = precio
        # self.cantidad = cantidad

    def editar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # def editarCantidad(self, nuevaCantidad):
    #     self.cantidad = nuevaCantidad

    def __repr__(self):
        return "Tipo: " + self.tipo + " Nombre: " + self.nombre + " Codigo : " + str(self.idProducto)

    def cumple(self, especificacion):
        dict_producto = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_producto or dict_producto[k] != especificacion.get_value(k):
                return False
        return True
