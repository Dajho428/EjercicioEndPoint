import uuid


class Accesorio:
    def __init__(self, tipo, nombre, precio=0):
        self.idAccesorio = uuid.uuid4()
        self.tipo = tipo
        self.nombre = nombre
        self.precio = precio

    def editar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # def editarCantidad(self, nuevaCantidad):
    #     self.cantidad = nuevaCantidad

    def __repr__(self):
        return "Tipo: " + self.tipo + " Nombre: " + self.nombre + " Codigo : " + str(self.idAccesorio)

    def cumple(self, especificacion):
        dict_accesorio = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_accesorio or dict_accesorio[k] != especificacion.get_value(k):
                return False
        return True
