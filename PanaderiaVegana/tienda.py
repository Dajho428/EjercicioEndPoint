import random
import string
import os

from PanaderiaVegana.Dominio.Bedidas import Bebida
from PanaderiaVegana.Dominio.Inventario import Inventario
from PanaderiaVegana.Dominio.Mesero import Mesero
from PanaderiaVegana.Dominio.Pan import Pan
from PanaderiaVegana.Dominio.Panadero import Panadero
from PanaderiaVegana.Dominio.Postre import Postre
from PanaderiaVegana.Infraestructura.Persistencia import Persistencia


if __name__ == '__main__':
    saver = Persistencia()
    saver.connect()
    nombreBebidas = ['Jugo Natural', 'limonada', 'agua']
    clasesPan = ['Croissant', 'Agridulce', 'Hawaiano']
    postres = ['Chocolate', 'Leche Vegetal', 'Dulce de Almendras']
    nombres = ['Juan', 'Carlos', 'Fernanda', 'Nathalia', 'Victoria', 'Andres']
    apellidos = ['Bedoya', 'Cardenas', 'Salazar', 'Restrepo', 'Fernandez']
    barrios = ['La fachada', 'Paraiso', 'Ciudad Dorada', 'Providencia', 'La Grecia',
               'Mercedes de Norte', 'Los Profesionales']
    # BEBIDA
    nombreBebida = random.choice(nombreBebidas)
    bebida = Bebida(nombreBebida)
    saver.guardar_bebida(bebida)
    Persistencia.save_json_bebida(bebida)
    # MESERO
    nombreMesero = random.choice(nombres)
    apellidoMesero = random.choice(apellidos)
    cedulaMesero = random.randint(1000000, 9999999)
    telefonoMesero = random.randint(1000000, 9999999)
    direccionMesero = "Barrio " + random.choice(barrios) + " Manzana " + random.choice(
        string.ascii_uppercase) + " Casa " + str(random.randint(0, 99))
    mesero = Mesero(nombreMesero, apellidoMesero, cedulaMesero, telefonoMesero, direccionMesero)
    saver.guardar_mesero(mesero)
    Persistencia.save_json_mesero(mesero)
    # PAN
    clasePan = random.choice(clasesPan)
    pan = Pan(clasePan)
    saver.guardar_pan(pan)
    Persistencia.save_json_pan(pan)
    # PANADERO
    nombrePanadero = random.choice(nombres)
    apellidoPanadero = random.choice(apellidos)
    cedulaPanadero = random.randint(1000000, 9999999)
    telefonoPanadero = random.randint(1000000, 9999999)
    direccionPanadero = "Barrio " + random.choice(barrios) + " Manzana " + random.choice(
        string.ascii_uppercase) + " Casa " + str(random.randint(0, 99))
    panadero = Panadero(nombrePanadero, apellidoPanadero, cedulaPanadero, telefonoPanadero, direccionPanadero)
    saver.guardar_panadero(panadero)
    Persistencia.save_json_panadero(panadero)
    # POSTRE
    nombrePostre = random.choice(postres)
    postre = Postre(nombrePostre)
    saver.guardar_postre(postre)
    Persistencia.save_json_postre(postre)
    inventario_json = Inventario()

    for file in os.listdir("./files"):
        if '.json' in file:
            inventario_json.agregar_mesero(Persistencia.load_json_mesero(file))
            inventario_json.agregar_bebida(Persistencia.load_json_bebida(file))
            inventario_json.agregar_pan(Persistencia.load_json_pan(file))
            inventario_json.agregar_panadero(Persistencia.load_json_panadero(file))
            inventario_json.agregar_postre(Persistencia.load_json_postre(file))
