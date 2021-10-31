import sqlite3

import jsonpickle

from PanaderiaVegana.Dominio.Bedidas import Bebida
from PanaderiaVegana.Dominio.Mesero import Mesero
from PanaderiaVegana.Dominio.Pan import Pan
from PanaderiaVegana.Dominio.Panadero import Panadero
from PanaderiaVegana.Dominio.Postre import Postre


class Persistencia():

    def connect(self):
        self.con = sqlite3.connect("Panadería Vegana.sqlite")
        self.__crear_tabla_bebidas()
        self.__crear_tabla_meseros()
        self.__crear_tabla_pan()
        self.__crear_tabla_panaderos()
        self.__crear_tabla_postres()

    def __crear_tabla_bebidas(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE BEBIDA(idBebida text primary key, nombreBebida text," \
                    " precio float) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_bebida(self, bebida: Bebida):
        cursor = self.con.cursor()
        query = "insert into BEBIDA(idBebida , nombreBebida ," \
                " precio  ) values(" \
                f" ?,?,?)"
        cursor.execute(query, (str(bebida.idBebida), bebida.nombreBebida, bebida.precio))
        self.con.commit()

    def __crear_tabla_meseros(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE MESERO(idMesero text primary key, nombre text," \
                    " apellido text, cedula text, telefono text, direccion text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_mesero(self, mesero: Mesero):
        cursor = self.con.cursor()
        query = "insert into MESERO(idMesero , nombre ," \
                " apellido , cedula , telefono, direccion ) values(" \
                f" ?,?,?,?,?,?)"
        cursor.execute(query, (str(mesero.idMesero), mesero.nombre, mesero.apellido,
                               mesero.cedula, mesero.telefono, mesero.direccion))
        self.con.commit()

    def __crear_tabla_pan(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE PAN(idPan text primary key, clase text," \
                    " precio float) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_pan(self, pan: Pan):
        cursor = self.con.cursor()
        query = "insert into PAN(idPan , clase ," \
                " precio ) values(" \
                f" ?,?,?)"
        cursor.execute(query, (str(pan.idPan), pan.clase, pan.precio))
        self.con.commit()

    def __crear_tabla_panaderos(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE PANADERO(idPanadero text primary key, nombre text," \
                    " apellido text, cedula text, telefono text, direccion text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_panadero(self, panadero: Panadero):
        cursor = self.con.cursor()
        query = "insert into PANADERO(idPanadero , nombre ," \
                " apellido , cedula , telefono, direccion ) values(" \
                f" ?,?,?,?,?,?)"
        cursor.execute(query, (str(panadero.idPanadero), panadero.nombre, panadero.apellido,
                               panadero.cedula, panadero.telefono, panadero.direccion))
        self.con.commit()

    def __crear_tabla_postres(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE POSTRE(idPostre text primary key, nombrePostre text," \
                    " precio float) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_postre(self, postre: Postre):
        cursor = self.con.cursor()
        query = "insert into POSTRE(idPostre , nombrePostre ," \
                " precio) values(" \
                f" ?,?,?)"
        cursor.execute(query, (str(postre.idPostre), postre.nombrePostre, postre.precio))
        self.con.commit()

    @classmethod
    def save_json_bebida(cls, bebida):
        text_open = open("files/"+str(bebida.idBebida) + '.json', mode='w')
        json_bebida = jsonpickle.encode(bebida)
        text_open.write(json_bebida)
        text_open.close()

    @classmethod
    def load_json_bebida(cls, file_name):
        text_open = open("files/"+file_name, mode='r')
        json_bebida = text_open.readline()
        bebida = jsonpickle.decode(json_bebida)
        text_open.close()
        return bebida

    @classmethod
    def save_json_mesero(cls, mesero):
        text_open = open("files/"+str(mesero.idMesero) + '.json', mode='w')
        json_mesero = jsonpickle.encode(mesero)
        text_open.write(json_mesero)
        text_open.close()

    @classmethod
    def load_json_mesero(cls, file_name):
        text_open = open("files/"+file_name, mode='r')
        json_mesero = text_open.readline()
        mesero = jsonpickle.decode(json_mesero)
        text_open.close()
        return mesero

    @classmethod
    def save_json_pan(cls, pan):
        text_open = open("files/"+str(pan.idPan) + '.json', mode='w')
        json_pan = jsonpickle.encode(pan)
        text_open.write(json_pan)
        text_open.close()

    @classmethod
    def load_json_pan(cls, file_name):
        text_open = open("files/"+file_name, mode='r')
        json_pan = text_open.readline()
        pan = jsonpickle.decode(json_pan)
        text_open.close()
        return pan

    @classmethod
    def save_json_panadero(cls, panadero):
        text_open = open("files/"+str(panadero.idPanadero) + '.json', mode='w')
        json_panadero = jsonpickle.encode(panadero)
        text_open.write(json_panadero)
        text_open.close()

    @classmethod
    def load_json_panadero(cls, file_name):
        text_open = open("files/"+file_name, mode='r')
        json_panadero = text_open.readline()
        panadero = jsonpickle.decode(json_panadero)
        text_open.close()
        return panadero

    @classmethod
    def save_json_postre(cls, postre):
        text_open = open("files/"+str(postre.idPostre) + '.json', mode='w')
        postre = jsonpickle.encode(postre)
        text_open.write(postre)
        text_open.close()

    @classmethod
    def load_json_postre(cls, file_name):
        text_open = open("files/"+file_name, mode='r')
        json_postre = text_open.readline()
        postre = jsonpickle.decode(json_postre)
        text_open.close()
        return postre
