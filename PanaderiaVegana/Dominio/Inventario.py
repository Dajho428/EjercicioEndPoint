from PanaderiaVegana.Dominio.Especificacion import Especificacion
from PanaderiaVegana.Dominio.Bedidas import Bebida
from PanaderiaVegana.Dominio.Mesero import Mesero
from PanaderiaVegana.Dominio.Pan import Pan
from PanaderiaVegana.Dominio.Panadero import Panadero
from PanaderiaVegana.Dominio.Postre import Postre


class Inventario():
    def __init__(self):
        self.bebidas = []
        self.pan = []
        self.postres = []
        self.panaderos = []
        self.meseros = []

    def agregar_bebida(self, bebida):
        if type(bebida) == Bebida:
            espec = Especificacion()
            espec.agregar_parametro('idBebida', bebida.idBebida)
            if len(list(self.buscar_bebida(espec))) == 0:
                self.bebidas.append(bebida)
            else:
                raise Exception('Bebida Existente')

    def buscar_bebida(self, especificacion):
        for g in self.bebidas:
            if g.cumple(especificacion):
                yield g

    def agregar_pan(self, pan):
        if type(pan) == Pan:
            espec = Especificacion()
            espec.agregar_parametro('idPan', pan.idPan)
            if len(list(self.buscar_pan(espec))) == 0:
                self.pan.append(pan)
            else:
                raise Exception('Pan Existente')

    def buscar_pan(self, especificacion):
        for g in self.pan:
            if g.cumple(especificacion):
                yield g

    def agregar_postre(self, postre):
        if type(postre) == Postre:
            espec = Especificacion()
            espec.agregar_parametro('idPostre', postre.idPostre)
            if len(list(self.buscar_postre(espec))) == 0:
                self.postres.append(postre)
            else:
                raise Exception('Postre Existente')

    def buscar_postre(self, especificacion):
        for g in self.postres:
            if g.cumple(especificacion):
                yield g

    def agregar_panadero(self, panadero):
        if type(panadero) == Panadero:
            espec = Especificacion()
            espec.agregar_parametro('idPostre', panadero.idPanadero)
            if len(list(self.buscar_panadero(espec))) == 0:
                self.panaderos.append(panadero)
            else:
                raise Exception('Panadero Existente')

    def buscar_panadero(self, especificacion):
        for g in self.panaderos:
            if g.cumple(especificacion):
                yield g

    def agregar_mesero(self, mesero):
        if type(mesero) == Mesero:
            espec = Especificacion()
            espec.agregar_parametro('idPMesero', mesero.idMesero)
            if len(list(self.buscar_mesero(espec))) == 0:
                self.meseros.append(mesero)
            else:
                raise Exception('Mesero Existente')

    def buscar_mesero(self, especificacion):
        for g in self.meseros:
            if g.cumple(especificacion):
                yield g
