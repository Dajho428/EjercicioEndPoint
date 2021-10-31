from TiendaMaquillaje.Dominio.Asesor import Asesor
from TiendaMaquillaje.Dominio.Cosmetico import Cosmetico
from TiendaMaquillaje.Dominio.Esmalte import Esmalte
from TiendaMaquillaje.Dominio.Especificacion import Especificacion
from TiendaMaquillaje.Dominio.Maquillaje import Maquillaje
from TiendaMaquillaje.Dominio.Perfume import Perfume


class Inventario():
    def __init__(self):
        self.asesores = []
        self.cosmeticos = []
        self.esmaltes = []
        self.maquillajes = []
        self.perfumes = []

    def agregar_asesor(self, asesor):
        if type(asesor) == Asesor:
            espec = Especificacion()
            espec.agregar_parametro('idAsesor', asesor.idAsesor)
            if len(list(self.buscar_asesor(espec))) == 0:
                self.asesores.append(asesor)
            else:
                raise Exception('asesor Existente')

    def buscar_asesor(self, especificacion):
        for g in self.asesores:
            if g.cumple(especificacion):
                yield g

    def agregar_cosmetico(self, cosmetico):
        if type(cosmetico) == Cosmetico:
            espec = Especificacion()
            espec.agregar_parametro('idCosmetico', cosmetico.idCosmetico)
            if len(list(self.buscar_cosmetico(espec))) == 0:
                self.cosmeticos.append(cosmetico)
            else:
                raise Exception('cosmetico Existente')

    def buscar_cosmetico(self, especificacion):
        for g in self.cosmeticos:
            if g.cumple(especificacion):
                yield g

    def agregar_esmalte(self, esmalte):
        if type(esmalte) == Esmalte:
            espec = Especificacion()
            espec.agregar_parametro('idEsmalte', esmalte.idEsmalte)
            if len(list(self.buscar_esmalte(espec))) == 0:
                self.esmaltes.append(esmalte)
            else:
                raise Exception('esmalte Existente')

    def buscar_esmalte(self, especificacion):
        for g in self.esmaltes:
            if g.cumple(especificacion):
                yield g

    def agregar_maquillaje(self, maquillaje):
        if type(maquillaje) == Maquillaje:
            espec = Especificacion()
            espec.agregar_parametro('idMaquillaje', maquillaje.idMaquillaje)
            if len(list(self.buscar_maquillaje(espec))) == 0:
                self.maquillajes.append(maquillaje)
            else:
                raise Exception('maquillaje Existente')

    def buscar_maquillaje(self, especificacion):
        for g in self.maquillajes:
            if g.cumple(especificacion):
                yield g

    def agregar_perfume(self, perfume):
        if type(perfume) == Perfume:
            espec = Especificacion()
            espec.agregar_parametro('idPerfume', perfume.idPerfume)
            if len(list(self.buscar_perfume(espec))) == 0:
                self.perfumes.append(perfume)
            else:
                raise Exception('maquillaje Existente')

    def buscar_perfume(self, especificacion):
        for g in self.perfumes:
            if g.cumple(especificacion):
                yield g
