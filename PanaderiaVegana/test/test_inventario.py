import random
import string

from PanaderiaVegana.Dominio.Bedidas import Bebida
from PanaderiaVegana.Dominio.Especificacion import Especificacion
from PanaderiaVegana.Dominio.Inventario import Inventario
from PanaderiaVegana.Dominio.Mesero import Mesero
from PanaderiaVegana.Dominio.Pan import Pan
from PanaderiaVegana.Dominio.Panadero import Panadero
from PanaderiaVegana.Dominio.Postre import Postre


def test_fuzzin_buscar():
    inventarioBebidas = Inventario()
    inventarioMesero = Inventario()
    inventarioPan = Inventario()
    inventarioPanadero = Inventario()
    inventarioPostre = Inventario()
    nombreBebidas = ['Jugo Natural', 'limonada', 'agua']
    clasesPan = ['Croissant', 'Agridulce', 'Hawaiano']
    postres = ['Chocolate', 'Leche Vegetal', 'Dulce de Almendras']
    nombres = ['Juan', 'Carlos', 'Fernanda', 'Nathalia', 'Victoria', 'Andres']
    apellidos = ['Bedoya', 'Cardenas', 'Salazar', 'Restrepo', 'Fernandez']
    barrios = ['La fachada', 'Paraiso', 'Ciudad Dorada', 'Providencia', 'La Grecia',
               'Mercedes de Norte', 'Los Profesionales']
    cantidadBebidas = random.randint(10, 100)
    cantidadMeseros = random.randint(10, 100)
    cantidadPanes = random.randint(10, 100)
    cantidadPanaderos = random.randint(10, 100)
    cantidadPostres = random.randint(10, 100)
    especificaciones_meseros = []
    especificaciones_bebidas=[]
    especificaciones_panes=[]
    especificaciones_panaderos=[]
    especificaciones_postres=[]
    # Bebidas
    for i in range(cantidadBebidas):
        nombreBebida = random.choice(nombreBebidas)
        if i % 10 == 0:
            especicificacion_bebida = Especificacion()
            especicificacion_bebida.agregar_parametro('nombreBebida', nombreBebida)
            especificaciones_bebidas.append(especicificacion_bebida)
        bebida = Bebida(nombreBebida)
        inventarioBebidas.agregar_bebida(bebida)
    cantidad_busquedas = random.randint(1, len(especificaciones_bebidas))
    for i in range(cantidad_busquedas):
        esp_beb = random.choice(especificaciones_bebidas)
        assert len(list(inventarioBebidas.buscar_bebida(esp_beb))) > 0
        print('encontrada')
        print(list(inventarioBebidas.buscar_bebida(esp_beb)))

    esp_fake_bebida = Especificacion()
    esp_fake_bebida.agregar_parametro('fabrica', 'postobon')
    print(inventarioBebidas.bebidas)
    assert len(list(inventarioBebidas.buscar_bebida(esp_fake_bebida))) == 0
    bebida = Bebida(nombreBebida)
    inventarioBebidas.agregar_bebida(bebida)
    try:
        inventarioBebidas.agregar_bebida(bebida)
        assert False
    except Exception as ex:
        assert ex

    # MESERO
    for i in range(cantidadMeseros):
        nombreMesero = random.choice(nombres)
        apellidoMesero = random.choice(apellidos)
        cedulaMesero = random.randint(1000000, 9999999)
        telefonoMesero = random.randint(1000000, 9999999)
        direccionMesero = "Barrio " + random.choice(barrios) + " Manzana " + random.choice(
            string.ascii_uppercase) + " Casa " + str(random.randint(0, 99))
        if i % 10 == 0:
            especicificacion_mesero = Especificacion()
            especicificacion_mesero.agregar_parametro('nombre', nombreMesero)
            especificaciones_meseros.append(especicificacion_mesero)
        mesero = Mesero(nombreMesero, apellidoMesero, cedulaMesero, telefonoMesero, direccionMesero)
        inventarioMesero.agregar_mesero(mesero)

    cantidad_busquedas = random.randint(1, len(especificaciones_meseros))
    for i in range(cantidad_busquedas):
        esp_mes = random.choice(especificaciones_meseros)
        assert len(list(inventarioMesero.buscar_mesero(esp_mes))) > 0
        print('encontrada')
        print(list(inventarioMesero.buscar_mesero(esp_mes)))

    esp_fake_mesero = Especificacion()
    esp_fake_mesero.agregar_parametro('correo', 'gmail')
    print(inventarioMesero.meseros)
    assert len(list(inventarioMesero.buscar_mesero(esp_fake_mesero))) == 0
    mesero = Mesero(nombreMesero,apellidoMesero,cedulaMesero,telefonoMesero,direccionMesero)
    inventarioMesero.agregar_mesero(mesero)
    try:
        inventarioMesero.agregar_mesero(mesero)
        assert False
    except Exception as ex:
        assert ex

    #PAN
    for i in range(cantidadPanes):
        clasePan = random.choice(clasesPan)
        if i % 10 == 0:
            especicificacion_pan = Especificacion()
            especicificacion_pan.agregar_parametro('clase', clasePan)
            especificaciones_panes.append(especicificacion_pan)
        pan = Pan(clasePan)
        inventarioPan.agregar_pan(pan)
    cantidad_busquedas = random.randint(1, len(especificaciones_panes))
    for i in range(cantidad_busquedas):
        esp_pan = random.choice(especificaciones_panes)
        assert len(list(inventarioPan.buscar_pan(esp_pan))) > 0
        print('encontrada')
        print(list(inventarioPan.buscar_pan(esp_pan)))

    esp_fake_pan = Especificacion()
    esp_fake_pan.agregar_parametro('sabor', 'chocolate')
    print(inventarioPan.pan)
    assert len(list(inventarioPan.buscar_pan(esp_fake_pan))) == 0
    pan = Pan(clasePan)
    inventarioPan.agregar_pan(pan)
    try:
        inventarioPan.agregar_pan(pan)
        assert False
    except Exception as ex:
        assert ex

    #PANADERO
    for i in range(cantidadPanaderos):
        nombrePanadero = random.choice(nombres)
        apellidoPanadero = random.choice(apellidos)
        cedulaPanadero = random.randint(1000000, 9999999)
        telefonoPanadero = random.randint(1000000, 9999999)
        direccionPanadero = "Barrio " + random.choice(barrios) + " Manzana " + random.choice(
            string.ascii_uppercase) + " Casa " + str(random.randint(0, 99))
        if i % 10 == 0:
            especicificacion_panadero = Especificacion()
            especicificacion_panadero.agregar_parametro('nombre', nombrePanadero)
            especificaciones_panaderos.append(especicificacion_panadero)
        panadero = Panadero(nombrePanadero, apellidoPanadero, cedulaPanadero, telefonoPanadero, direccionPanadero)
        inventarioPanadero.agregar_panadero(panadero)

    cantidad_busquedas = random.randint(1, len(especificaciones_panaderos))
    for i in range(cantidad_busquedas):
        esp_panadero = random.choice(especificaciones_panaderos)
        assert len(list(inventarioPanadero.buscar_panadero(esp_panadero))) > 0
        print('encontrada')
        print(list(inventarioPanadero.buscar_panadero(esp_panadero)))

    esp_fake_panadero = Especificacion()
    esp_fake_panadero.agregar_parametro('correo', 'gmail')
    print(inventarioPanadero.panaderos)
    assert len(list(inventarioPanadero.buscar_panadero(esp_fake_panadero))) == 0
    panadero = Panadero(nombrePanadero, apellidoPanadero, cedulaPanadero, telefonoPanadero, direccionPanadero)
    inventarioPanadero.agregar_panadero(panadero)
    try:
        inventarioPanadero.agregar_panadero(panadero)
        assert False
    except Exception as ex:
        assert ex

    #POSTRES
    for i in range(cantidadPostres):
        nombrePostre = random.choice(postres)
        if i % 10 == 0:
            especicificacion_postre = Especificacion()
            especicificacion_postre.agregar_parametro('nombrePostre', nombrePostre)
            especificaciones_postres.append(especicificacion_postre)
        postre = Postre(nombrePostre)
        inventarioPostre.agregar_postre(postre)
    cantidad_busquedas = random.randint(1, len(especificaciones_postres))
    for i in range(cantidad_busquedas):
        esp_postre = random.choice(especificaciones_postres)
        assert len(list(inventarioPostre.buscar_postre(esp_postre))) > 0
        print('encontrada')
        print(list(inventarioPostre.buscar_postre(esp_postre)))

    esp_fake_postre = Especificacion()
    esp_fake_postre.agregar_parametro('sabor', 'miloja')
    print(inventarioPostre.postres)
    assert len(list(inventarioPostre.buscar_postre(esp_fake_postre))) == 0
    postre = Postre(nombrePostre)
    inventarioPostre.agregar_postre(postre)
    try:
        inventarioPostre.agregar_postre(postre)
        assert False
    except Exception as ex:
        assert ex


if __name__ == '__main__':
    test_fuzzin_buscar()
