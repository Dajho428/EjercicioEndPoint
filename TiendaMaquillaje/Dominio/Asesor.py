import uuid


class Asesor:
    def __init__(self, nombre, apellido, cedula, telefono, direccion):
        self.idAsesor = uuid.uuid4()
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.telefono = telefono
        self.direccion = direccion

    def editar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono

    def editar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion

    def __repr__(self):
        return "Asesor: " + self.nombre + " Codigo: " + str(self.idAsesor)

    def cumple(self, especificacion):
        dict_asesor = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_asesor or dict_asesor[k] != especificacion.get_value(k):
                return False
        return True
