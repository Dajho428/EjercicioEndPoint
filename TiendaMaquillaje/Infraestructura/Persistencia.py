import sqlite3
import jsonpickle

from TiendaMaquillaje.Dominio.Asesor import Asesor
from TiendaMaquillaje.Dominio.Cosmetico import Cosmetico
from TiendaMaquillaje.Dominio.Esmalte import Esmalte
from TiendaMaquillaje.Dominio.Maquillaje import Maquillaje
from TiendaMaquillaje.Dominio.Perfume import Perfume


class Persistencia():

    def connect(self):
        self.con = sqlite3.connect("Tienda Maquillaje.sqlite")
        self.__crear_tabla_asesores()
        self.__crear_tabla_cosmeticos()
        self.__crear_tabla_esmaltes()
        self.__crear_tabla_maquillajes()
        self.__crear_tabla_perfumes()

    def __crear_tabla_asesores(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE ASESOR(idAsesor text primary key, nombre text," \
                    " apellido text, cedula text, telefono text, direccion text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_asesor(self, asesor: Asesor):
        cursor = self.con.cursor()
        query = "insert into ASESOR(idAsesor , nombre ," \
                " apellido , cedula , telefono, direccion ) values(" \
                f" ?,?,?,?,?,?)"
        cursor.execute(query, (str(asesor.idAsesor), asesor.nombre, asesor.apellido,
                               asesor.cedula, asesor.telefono, asesor.direccion))
        self.con.commit()

    def __crear_tabla_cosmeticos(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE COSMETICO(idCosmetico text primary key, tipo text," \
                    " nombre text,precio float) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_cosmetico(self, cosmetico: Cosmetico):
        cursor = self.con.cursor()
        query = "insert into COSMETICO(idCosmetico , tipo ," \
                " nombre, precio) values(" \
                f" ?,?,?,?)"
        cursor.execute(query, (str(cosmetico.idCosmetico), cosmetico.tipo, cosmetico.nombre, cosmetico.precio))
        self.con.commit()

    def __crear_tabla_esmaltes(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE ESMALTE(idEsmalte text primary key, marca text," \
                    " color text,precio float) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_esmalte(self, esmalte: Esmalte):
        cursor = self.con.cursor()
        query = "insert into ESMALTE(idEsmalte , marca ," \
                " color , precio) values(" \
                f" ?,?,?,?)"
        cursor.execute(query, (str(esmalte.idEsmalte), esmalte.marca, esmalte.color, esmalte.precio))
        self.con.commit()

    def __crear_tabla_maquillajes(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE MAQUILLAJE(idMaquillaje text primary key, tipo text," \
                    " nombre text,precio float) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_maquillaje(self, maquillaje: Maquillaje):
        cursor = self.con.cursor()
        query = "insert into MAQUILLAJE(idMaquillaje , tipo ," \
                " nombre, precio) values(" \
                f" ?,?,?,?)"
        cursor.execute(query, (str(maquillaje.idMaquillaje), maquillaje.tipo, maquillaje.nombre, maquillaje.precio))
        self.con.commit()

    def __crear_tabla_perfumes(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE PERFUME(idPerfume text primary key, fabricante text," \
                    " nombre text,precio float) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_perfume(self, perfume: Perfume):
        cursor = self.con.cursor()
        query = "insert into PERFUME(idPerfume , fabricante ," \
                " nombre, precio) values(" \
                f" ?,?,?,?)"
        cursor.execute(query, (str(perfume.idPerfume), perfume.fabricante, perfume.nombre, perfume.precio))
        self.con.commit()

    @classmethod
    def save_json_asesor(cls, asesor):
        text_open = open("files/" + str(asesor.idAsesor) + '.json', mode='w')
        json_asesor = jsonpickle.encode(asesor)
        text_open.write(json_asesor)
        text_open.close()

    @classmethod
    def load_json_asesor(cls, file_name):
        text_open = open("files/"+file_name, mode='r')
        json_asesor = text_open.readline()
        asesor = jsonpickle.decode(json_asesor)
        text_open.close()
        return asesor

    @classmethod
    def save_json_cosmetico(cls, cosmetico):
        text_open = open("files/" + str(cosmetico.idCosmetico) + '.json', mode='w')
        json_cosmetico = jsonpickle.encode(cosmetico)
        text_open.write(json_cosmetico)
        text_open.close()

    @classmethod
    def load_json_cosmetico(cls, file_name):
        text_open = open("files/"+file_name, mode='r')
        json_cosmetico = text_open.readline()
        cosmetico = jsonpickle.decode(json_cosmetico)
        text_open.close()
        return cosmetico

    @classmethod
    def save_json_esmalte(cls, esmalte):
        text_open = open("files/" + str(esmalte.idEsmalte) + '.json', mode='w')
        json_esmalte = jsonpickle.encode(esmalte)
        text_open.write(json_esmalte)
        text_open.close()

    @classmethod
    def load_json_esmalte(cls, file_name):
        text_open = open("files/"+file_name, mode='r')
        json_esmalte = text_open.readline()
        esmalte = jsonpickle.decode(json_esmalte)
        text_open.close()
        return esmalte

    @classmethod
    def save_json_maquillaje(cls, maquillaje):
        text_open = open("files/" + str(maquillaje.idMaquillaje) + '.json', mode='w')
        json_maquillaje = jsonpickle.encode(maquillaje)
        text_open.write(json_maquillaje)
        text_open.close()

    @classmethod
    def load_json_maquillaje(cls, file_name):
        text_open = open("files/"+file_name, mode='r')
        json_maquillaje = text_open.readline()
        maquillaje = jsonpickle.decode(json_maquillaje)
        text_open.close()
        return maquillaje

    @classmethod
    def save_json_perfume(cls, perfume):
        text_open = open("files/" + str(perfume.idPerfume) + '.jsonPerfume', mode='w')
        json_perfume = jsonpickle.encode(perfume)
        text_open.write(json_perfume)
        text_open.close()

    @classmethod
    def load_json_perfume(cls, file_name):
        text_open = open("files/"+file_name, mode='r')
        json_perfume = text_open.readline()
        perfume = jsonpickle.decode(json_perfume)
        text_open.close()
        return perfume
