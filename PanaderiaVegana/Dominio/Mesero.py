import uuid


class Mesero:
    def __init__(self, nombre, apellido, cedula, telefono, direccion):
        self.idMesero = uuid.uuid4()
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.telefono = telefono
        self.direccion = direccion

    def editarTelefono(self, nuevoTelefono):
        self.telefono = nuevoTelefono

    def editarDireccion(self, nuevaDireccion):
        self.direccion = nuevaDireccion

    def __repr__(self):
        return "Mesero: "+self.nombre+" Codigo: " + str(self.idMesero)

    def cumple(self, especificacion):
        dict_mesero = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_mesero or dict_mesero[k] != especificacion.get_value(k):
                return False
        return True
