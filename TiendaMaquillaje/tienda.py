import os
import random
import string

from TiendaMaquillaje.Dominio.Asesor import Asesor
from TiendaMaquillaje.Dominio.Cosmetico import Cosmetico
from TiendaMaquillaje.Dominio.Esmalte import Esmalte
from TiendaMaquillaje.Dominio.Inventario import Inventario
from TiendaMaquillaje.Dominio.Maquillaje import Maquillaje
from TiendaMaquillaje.Dominio.Perfume import Perfume
from TiendaMaquillaje.Infraestructura.Persistencia import Persistencia

if __name__ == '__main__':
    saver = Persistencia()
    saver.connect()
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
    # ASESOR
    nombreAsesor = random.choice(nombres)
    apellidoAsesor = random.choice(apellidos)
    cedulaAsesor = random.randint(1000000, 9999999)
    telefonoAsesor = random.randint(1000000, 9999999)
    direccionAsesor = "Barrio " + random.choice(barrios) + " Manzana " + random.choice(
        string.ascii_uppercase) + " Casa " + str(random.randint(0, 99))
    asesor = Asesor(nombreAsesor, apellidoAsesor, cedulaAsesor, telefonoAsesor, direccionAsesor)
    saver.guardar_asesor(asesor)
    Persistencia.save_json_asesor(asesor)
    # COSMETICO
    tipoCosmetico = random.choice(tipoCosmeticos)
    nombreCosmetico = random.choice(nombresCosmeticos[tipoCosmetico])
    cosmetico = Cosmetico(tipoCosmetico, nombreCosmetico)
    saver.guardar_cosmetico(cosmetico)
    Persistencia.save_json_cosmetico(cosmetico)
    # ESMALTE
    marcaEsmalte = random.choice(marcasEsmaltes)
    colorEsmalte = random.choice(coloresEsmaltes)
    esmalte = Esmalte(marcaEsmalte, colorEsmalte)
    saver.guardar_esmalte(esmalte)
    Persistencia.save_json_esmalte(esmalte)
    # MAQUILLAJE
    tipoMaquillaje = random.choice(tiposMaquillajes)
    nombreMaquillaje = random.choice(nombresMaquillajes[tipoMaquillaje])
    maquillaje = Maquillaje(tipoMaquillaje, nombreMaquillaje)
    saver.guardar_maquillaje(maquillaje)
    Persistencia.save_json_maquillaje(maquillaje)
    # PERFUME
    fabricantePerfume = random.choice(fabricantesPerfumes)
    nombrePerfume = random.choice(nombresPerfumes[fabricantePerfume])
    perfume = Perfume(fabricantePerfume, nombrePerfume)
    saver.guardar_perfume(perfume)
    Persistencia.save_json_perfume(perfume)

    inventario_json = Inventario()
    for file in os.listdir("./files"):
        if '.json' in file:
            inventario_json.agregar_asesor(Persistencia.load_json_asesor(file))
            inventario_json.agregar_cosmetico(Persistencia.load_json_cosmetico(file))
            inventario_json.agregar_esmalte(Persistencia.load_json_esmalte(file))
            inventario_json.agregar_maquillaje(Persistencia.load_json_maquillaje(file))
            inventario_json.agregar_perfume(Persistencia.load_json_perfume(file))
