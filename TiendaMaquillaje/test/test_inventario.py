import random
import string

from TiendaMaquillaje.Dominio.Asesor import Asesor
from TiendaMaquillaje.Dominio.Cosmetico import Cosmetico
from TiendaMaquillaje.Dominio.Esmalte import Esmalte
from TiendaMaquillaje.Dominio.Especificacion import Especificacion
from TiendaMaquillaje.Dominio.Inventario import Inventario
from TiendaMaquillaje.Dominio.Maquillaje import Maquillaje
from TiendaMaquillaje.Dominio.Perfume import Perfume


def test_fuzzin_buscar():
    inventarioAsesores = Inventario()
    inventarioCosmeticos = Inventario()
    inventarioEsmaltes = Inventario()
    inventarioMaquillajes = Inventario()
    inventarioPerfumes = Inventario()
    nombres = ['Juan', 'Carlos', 'Fernanda', 'Nathalia', 'Victoria', 'Andres']
    apellidos = ['Bedoya', 'Cardemas', 'Salazar', 'Restrepo', 'Fernandez']
    barrios = ['La fachada', 'Paraiso', 'Ciudad Dorada', 'Providencia', 'La Grecia',
               'Mercedes de Norte', 'Los Profesionales']
    tipoCosmeticos = ['Lociones Faciales', 'Cremas Hidratantes', 'Cremas Rejuvenecedoras', 'Mascarillas']
    nombresCosmeticos = {
        'Lociones Faciales': ['Crema Facial Q10 Antiarrugas', 'Hydro Boost Gel Cream', 'Hydrance Optimale Ligère'],
        'Cremas Hidratantes': ['Dramatically Different', 'Colágeno Nutritiva', 'Ultra Facial Oil Free Gel Cream'],
        'Cremas Rejuvenecedoras': ['Elizabeth Arden Prevage Anti Aging Overnight', 'Nivea Crema Anti-Arrugas Dia'],
        'Mascarillas': ['Máscaras de hidrogel', 'Mascarillas en crema']
    }
    marcasEsmaltes = ['Vogue', 'Masglo', 'Admiss']
    coloresEsmaltes = ['Azul', 'Rojo', 'Verde', 'Naranja', 'Amarillo', 'Cafe', 'Blanco', 'Negro']
    tiposMaquillajes = ['Rubor', 'Polvo Facial', 'Pestañina']
    nombresMaquillajes = {
        'Rubor': ['Powder Blush', 'Baked Blush 03'],
        'Polvo Facial': ['Nailen', 'Almay', 'Colorstay'],
        'Pestañina': ['Vogue eyes', 'Roller Lash']
    }
    fabricantesPerfumes = ['Paco Rabanne', 'Dolce & Gabbana', 'Hugo Boss']
    nombresPerfumes = {
        'Paco Rabanne': ['1 Million', 'Ultraviolet'],
        'Dolce & Gabbana': ['Light Blue', 'D&G', 'Rose The One'],
        'Hugo Boss': ['Just Different', 'Bottled', 'Orange Man']
    }
    cantidadAsesores = random.randint(10, 100)
    cantidadCosmeticos = random.randint(10, 100)
    cantidadEsmaltes = random.randint(10, 100)
    cantidadMaquillajes = random.randint(10, 100)
    cantidadPerfumes = random.randint(10, 100)
    especificaciones_asesores = []
    especificaciones_cosmeticos = []
    especificaciones_esmaltes = []
    especificaciones_maquillajes = []
    especificaciones_perfumes = []
    # ASESOR
    for i in range(cantidadAsesores):
        nombreAsesor = random.choice(nombres)
        apellidoAsesor = random.choice(apellidos)
        cedulaAsesor = random.randint(1000000, 9999999)
        telefonoAsesor = random.randint(1000000, 9999999)
        direccionAsesor = "Barrio " + random.choice(barrios) + " Manzana " + random.choice(
            string.ascii_uppercase) + " Casa " + str(random.randint(0, 99))
        if i % 10 == 0:
            especicificacion_asesor = Especificacion()
            especicificacion_asesor.agregar_parametro('nombre', nombreAsesor)
            especificaciones_asesores.append(especicificacion_asesor)
        asesor = Asesor(nombreAsesor, apellidoAsesor, cedulaAsesor, telefonoAsesor, direccionAsesor)
        inventarioAsesores.agregar_asesor(asesor)

    cantidad_busquedas = random.randint(1, len(especificaciones_asesores))
    for i in range(cantidad_busquedas):
        esp_asesor = random.choice(especificaciones_asesores)
        assert len(list(inventarioAsesores.buscar_asesor(esp_asesor))) > 0
        print('encontrada')
        print(list(inventarioAsesores.buscar_asesor(esp_asesor)))

    esp_fake_asesor = Especificacion()
    esp_fake_asesor.agregar_parametro('correo', 'gmail')
    print(inventarioAsesores.asesores)
    assert len(list(inventarioAsesores.buscar_asesor(esp_fake_asesor))) == 0
    asesor = Asesor(nombreAsesor, apellidoAsesor, cedulaAsesor, telefonoAsesor, direccionAsesor)
    inventarioAsesores.agregar_asesor(asesor)
    try:
        inventarioAsesores.agregar_asesor(asesor)
        assert False
    except Exception as ex:
        assert ex
    # COSMETICO
    for i in range(cantidadCosmeticos):
        tipoCosmetico = random.choice(tipoCosmeticos)
        nombreCosmetico = random.choice(nombresCosmeticos[tipoCosmetico])
        if i % 10 == 0:
            especificacion_cosmetico = Especificacion()
            especificacion_cosmetico.agregar_parametro('tipo', tipoCosmetico)
            especificacion_cosmetico.agregar_parametro('nombre', nombreCosmetico)
            especificaciones_cosmeticos.append(especificacion_cosmetico)
        cosmetico = Cosmetico(tipoCosmetico, nombreCosmetico)
        inventarioCosmeticos.agregar_cosmetico(cosmetico)
    cantidad_busquedas = random.randint(1, len(especificaciones_cosmeticos))
    for i in range(cantidad_busquedas):
        esp_cosmetico = random.choice(especificaciones_cosmeticos)
        assert len(list(inventarioCosmeticos.buscar_cosmetico(esp_cosmetico))) > 0
        print('encontrada')
        print(list(inventarioCosmeticos.buscar_cosmetico(esp_cosmetico)))

    esp_fake_cosm = Especificacion()
    esp_fake_cosm.agregar_parametro('color', 'verde')
    print(inventarioCosmeticos.cosmeticos)
    assert len(list(inventarioCosmeticos.buscar_cosmetico(esp_fake_cosm))) == 0
    cosmetico = Cosmetico(tipoCosmetico, nombreCosmetico)
    inventarioCosmeticos.agregar_cosmetico(cosmetico)
    try:
        inventarioCosmeticos.agregar_cosmetico(cosmetico)
        assert False
    except Exception as ex:
        assert ex
    # ESMALTES
    for i in range(cantidadEsmaltes):
        marca = random.choice(marcasEsmaltes)
        color = random.choice(coloresEsmaltes)
        if i % 10 == 0:
            especificacion_esmalte = Especificacion()
            especificacion_esmalte.agregar_parametro('marca', marca)
            especificacion_esmalte.agregar_parametro('color', color)
            especificaciones_esmaltes.append(especificacion_esmalte)
        esmalte = Esmalte(marca, color)
        inventarioEsmaltes.agregar_esmalte(esmalte)
    cantidad_busquedas = random.randint(1, len(especificaciones_esmaltes))
    for i in range(cantidad_busquedas):
        esp_esmalte = random.choice(especificaciones_esmaltes)
        assert len(list(inventarioEsmaltes.buscar_esmalte(esp_esmalte))) > 0
        print('encontrada')
        print(list(inventarioEsmaltes.buscar_esmalte(esp_esmalte)))

    esp_fake_esmalte = Especificacion()
    esp_fake_esmalte.agregar_parametro('tamaño', 'grande')
    print(inventarioEsmaltes.esmaltes)
    assert len(list(inventarioEsmaltes.buscar_esmalte(esp_fake_esmalte))) == 0
    esmalte = Esmalte(marca, color)
    inventarioEsmaltes.agregar_esmalte(esmalte)
    try:
        inventarioEsmaltes.agregar_esmalte(esmalte)
        assert False
    except Exception as ex:
        assert ex
    #MAQUILLAJE
    for i in range(cantidadMaquillajes):
        tipoMaquillaje = random.choice(tiposMaquillajes)
        nombreMaquillaje = random.choice(nombresMaquillajes[tipoMaquillaje])
        if i % 10 == 0:
            especificacion_maquillaje = Especificacion()
            especificacion_maquillaje.agregar_parametro('tipo', tipoMaquillaje)
            especificacion_maquillaje.agregar_parametro('nombre', nombreMaquillaje)
            especificaciones_maquillajes.append(especificacion_maquillaje)
        maquillaje = Maquillaje(tipoMaquillaje,nombreMaquillaje )
        inventarioMaquillajes.agregar_maquillaje(maquillaje)

    cantidad_busquedas = random.randint(1, len(especificaciones_maquillajes))
    for i in range(cantidad_busquedas):
        esp_maquillaje = random.choice(especificaciones_maquillajes)
        assert len(list(inventarioMaquillajes.buscar_maquillaje(esp_maquillaje))) > 0
        print('encontrada')
        print(list(inventarioMaquillajes.buscar_maquillaje(esp_maquillaje)))

    esp_fake_maq = Especificacion()
    esp_fake_maq.agregar_parametro('tamaño', 'grande')
    print(inventarioMaquillajes.maquillajes)
    assert len(list(inventarioMaquillajes.buscar_maquillaje(esp_fake_maq))) == 0
    maquillaje = Maquillaje(tipoMaquillaje,nombreMaquillaje)
    inventarioMaquillajes.agregar_maquillaje(maquillaje)
    try:
        inventarioMaquillajes.agregar_maquillaje(maquillaje)
        assert False
    except Exception as ex:
        assert ex
    #PERFUME
    for i in range(cantidadPerfumes):
        fabricante = random.choice(fabricantesPerfumes)
        nombre = random.choice(nombresPerfumes[fabricante])
        if i % 10 == 0:
            especificacion_perfume = Especificacion()
            especificacion_perfume.agregar_parametro('fabricante', fabricante)
            especificacion_perfume.agregar_parametro('nombre', nombre)
            especificaciones_perfumes.append(especificacion_perfume)
        perfume = Perfume(fabricante,nombre )
        inventarioPerfumes.agregar_perfume(perfume)

    cantidad_busquedas = random.randint(1, len(especificaciones_perfumes))
    for i in range(cantidad_busquedas):
        esp_perfume = random.choice(especificaciones_perfumes)
        assert len(list(inventarioPerfumes.buscar_perfume(esp_perfume))) > 0
        print('encontrada')
        print(list(inventarioPerfumes.buscar_perfume(esp_perfume)))

    esp_fake_perfume = Especificacion()
    esp_fake_perfume.agregar_parametro('tamaño', 'grande')
    print(inventarioPerfumes.perfumes)
    assert len(list(inventarioPerfumes.buscar_perfume(esp_fake_perfume))) == 0
    perfume = Perfume(fabricante,nombre)
    inventarioPerfumes.agregar_perfume(perfume)
    try:
        inventarioPerfumes.agregar_perfume(perfume)
        assert False
    except Exception as ex:
        assert ex

if __name__ == '__main__':
    test_fuzzin_buscar()
