import uuid


class Panadero:
    def __init__(self, nombre, apellido, cedula, telefono, direccion):
        self.idPanadero = uuid.uuid4()
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
        return "Panadero: "+self.nombre+" Codigo: " + str(self.idPanadero)

    def cumple(self, especificacion):
        dict_panadero = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_panadero or dict_panadero[k] != especificacion.get_value(k):
                return False
        return True
