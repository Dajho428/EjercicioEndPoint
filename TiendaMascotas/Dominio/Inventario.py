from PanaderiaVegana.Dominio.Especificacion import Especificacion
from TiendaMascotas.Dominio.Accesorio import Accesorio
from TiendaMascotas.Dominio.AlimentoMascota import AlimentoMascota
from TiendaMascotas.Dominio.PeluqueriaCanina import PeluqueriaCanina
from TiendaMascotas.Dominio.ProductoAseoMascota import ProductoAseoMascota
from TiendaMascotas.Dominio.VentaMascota import VentaMascota


class Inventario():
    def __init__(self):
        self.accesorios = []
        self.alimentos = []
        self.peluqueria = []
        self.productos = []
        self.ventas = []

    def agregar_accesorio(self, accesorio):
        if type(accesorio) == Accesorio:
            espec = Especificacion()
            espec.agregar_parametro('idAccesorio', accesorio.idAccesorio)
            if len(list(self.buscar_accesorio(espec))) == 0:
                self.accesorios.append(accesorio)
            else:
                raise Exception('accesorio Existente')

    def buscar_accesorio(self, especificacion):
        for g in self.accesorios:
            if g.cumple(especificacion):
                yield g

    def agregar_alimento(self, alimento):
        if type(alimento) == AlimentoMascota:
            espec = Especificacion()
            espec.agregar_parametro('idAlimento', alimento.idAlimento)
            if len(list(self.buscar_alimento(espec))) == 0:
                self.alimentos.append(alimento)
            else:
                raise Exception('alimento Existente')

    def buscar_alimento(self, especificacion):
        for g in self.alimentos:
            if g.cumple(especificacion):
                yield g

    def agregar_peluqueria(self, peluqueriaCanina):
        if type(peluqueriaCanina) == PeluqueriaCanina:
            espec = Especificacion()
            espec.agregar_parametro('idMascosta', peluqueriaCanina.idMascota)
            if len(list(self.buscar_peluqueria(espec))) == 0:
                self.peluqueria.append(peluqueriaCanina)
            else:
                raise Exception('peluqueria Existente')

    def buscar_peluqueria(self, especificacion):
        for g in self.peluqueria:
            if g.cumple(especificacion):
                yield g

    def agregar_producto(self, productoAseoMascota):
        if type(productoAseoMascota) == ProductoAseoMascota:
            espec = Especificacion()
            espec.agregar_parametro('idProducto', productoAseoMascota.idProducto)
            if len(list(self.buscar_producto(espec))) == 0:
                self.productos.append(productoAseoMascota)
            else:
                raise Exception('producto Existente')

    def buscar_producto(self, especificacion):
        for g in self.productos:
            if g.cumple(especificacion):
                yield g

    def agregar_venta(self, ventaMascota):
        if type(ventaMascota) == VentaMascota:
            espec = Especificacion()
            espec.agregar_parametro('idVentaMascota', ventaMascota.idVentaMascota)
            if len(list(self.buscar_venta(espec))) == 0:
                self.ventas.append(ventaMascota)
            else:
                raise Exception('Venta Existente')

    def buscar_venta(self, especificacion):
        for g in self.ventas:
            if g.cumple(especificacion):
                yield g
