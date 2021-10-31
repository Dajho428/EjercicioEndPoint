import sqlite3

import jsonpickle

from TiendaMascotas.Dominio.Accesorio import Accesorio
from TiendaMascotas.Dominio.AlimentoMascota import AlimentoMascota
from TiendaMascotas.Dominio.PeluqueriaCanina import PeluqueriaCanina
from TiendaMascotas.Dominio.ProductoAseoMascota import ProductoAseoMascota
from TiendaMascotas.Dominio.VentaMascota import VentaMascota


class Persistencia():

    def connect(self):
        self.con = sqlite3.connect("Tienda Mascota.sqlite")
        self.__crear_tabla_accesorios()
        self.__crear_tabla_alimentos()
        self.__crear_tabla_peluqueria()
        self.__crear_tabla_productos()
        self.__crear_tabla_ventas()

    def __crear_tabla_accesorios(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE ACCESORIOS(idAccesorio text primary key, tipo text," \
                    " nombre text,precio float) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_accesorio(self, accesorio: Accesorio):
        cursor = self.con.cursor()
        query = "insert into ACCESORIOS(idAccesorio ,tipo, nombre ," \
                " precio  ) values(" \
                f" ?,?,?,?)"
        cursor.execute(query, (str(accesorio.idAccesorio), accesorio.tipo, accesorio.nombre, accesorio.precio))
        self.con.commit()

    def __crear_tabla_alimentos(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE ALIMENTOS(idAlimento text primary key, tipo text," \
                    " nombre text,precio float) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_alimento(self, alimento: AlimentoMascota):
        cursor = self.con.cursor()
        query = "insert into ALIMENTOS(idAlimento ,tipo, nombre ," \
                " precio  ) values(" \
                f" ?,?,?,?)"
        cursor.execute(query, (str(alimento.idAlimento), alimento.tipo, alimento.nombre, alimento.precio))
        self.con.commit()

    def __crear_tabla_peluqueria(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE PELUQUERIA(idMascota text primary key," \
                    " nombre text,precio float) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_peluqueria(self, peluqueria: PeluqueriaCanina):
        cursor = self.con.cursor()
        query = "insert into PELUQUERIA(idMascota , nombre ," \
                " precio  ) values(" \
                f" ?,?,?)"
        cursor.execute(query, (str(peluqueria.idMascota), peluqueria.nombre, peluqueria.precio))
        self.con.commit()

    def __crear_tabla_productos(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE PRODUCTOS(idProducto text primary key,tipo text," \
                    " nombre text,precio float) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_producto(self, producto: ProductoAseoMascota):
        cursor = self.con.cursor()
        query = "insert into PRODUCTOS(idProducto ,tipo, nombre ," \
                " precio  ) values(" \
                f" ?,?,?,?)"
        cursor.execute(query, (str(producto.idProducto), producto.tipo, producto.nombre, producto.precio))
        self.con.commit()

    def __crear_tabla_ventas(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE VENTAS(idVentaMascota text primary key,tipo text," \
                    " raza text,precio float) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_venta(self, venta: VentaMascota):
        cursor = self.con.cursor()
        query = "insert into VENTAS(idVentaMascota ,tipo, raza ," \
                " precio  ) values(" \
                f" ?,?,?,?)"
        cursor.execute(query, (str(venta.idVentaMascota), venta.tipo, venta.raza, venta.precio))
        self.con.commit()

    @classmethod
    def save_json_accesorio(cls, accesorio):
        text_open = open("files/" + str(accesorio.idAccesorio) + '.json', mode='w')
        json_accesorio = jsonpickle.encode(accesorio)
        text_open.write(json_accesorio)
        text_open.close()

    @classmethod
    def load_json_accesorio(cls, file_name):
        text_open = open("files/"+file_name, mode='r')
        json_accesorio = text_open.readline()
        accesorio = jsonpickle.decode(json_accesorio)
        text_open.close()
        return accesorio

    @classmethod
    def save_json_alimento(cls, alimentoMascota):
        text_open = open("files/" + str(alimentoMascota.idAlimento) + '.json', mode='w')
        json_alimento = jsonpickle.encode(alimentoMascota)
        text_open.write(json_alimento)
        text_open.close()

    @classmethod
    def load_json_alimento(cls, file_name):
        text_open = open("files/"+file_name, mode='r')
        json_alimento = text_open.readline()
        alimento = jsonpickle.decode(json_alimento)
        text_open.close()
        return alimento

    @classmethod
    def save_json_peluqueria(cls, peluqueriaCanina):
        text_open = open("files/" + str(peluqueriaCanina.idMascota) + '.json', mode='w')
        json_peluqueria = jsonpickle.encode(peluqueriaCanina)
        text_open.write(json_peluqueria)
        text_open.close()

    @classmethod
    def load_json_peluqueria(cls, file_name):
        text_open = open("files/"+file_name, mode='r')
        json_peluqueria = text_open.readline()
        peluqueria = jsonpickle.decode(json_peluqueria)
        text_open.close()
        return peluqueria

    @classmethod
    def save_json_producto(cls, producto):
        text_open = open("files/" + str(producto.idProducto) + '.json', mode='w')
        json_producto = jsonpickle.encode(producto)
        text_open.write(json_producto)
        text_open.close()

    @classmethod
    def load_json_producto(cls, file_name):
        text_open = open("files/"+file_name, mode='r')
        json_producto = text_open.readline()
        producto = jsonpickle.decode(json_producto)
        text_open.close()
        return producto

    @classmethod
    def save_json_venta(cls, venta):
        text_open = open("files/" + str(venta.idVentaMascota) + '.json', mode='w')
        json_venta = jsonpickle.encode(venta)
        text_open.write(json_venta)
        text_open.close()

    @classmethod
    def load_json_venta(cls, file_name):
        text_open = open("files/"+file_name, mode='r')
        json_venta = text_open.readline()
        venta = jsonpickle.decode(json_venta)
        text_open.close()
        return venta
