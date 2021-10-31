import os
import random

from TiendaMascotas.Dominio.Accesorio import Accesorio
from TiendaMascotas.Dominio.AlimentoMascota import AlimentoMascota
from TiendaMascotas.Dominio.Inventario import Inventario
from TiendaMascotas.Dominio.PeluqueriaCanina import PeluqueriaCanina
from TiendaMascotas.Dominio.ProductoAseoMascota import ProductoAseoMascota
from TiendaMascotas.Dominio.VentaMascota import VentaMascota
from TiendaMascotas.Infraestructura.Persistencia import Persistencia

if __name__ == '__main__':
    saver = Persistencia()
    saver.connect()
    tiposAccesorios = ['Collar Gatos', 'Collar Perros', 'Juguetes']
    nombresAccesorios = {
        'Collar Gatos': ['De seguro', 'De Broche', 'Isabelino'],
        'Collar Perros': ['De taches', 'Pechera', 'Correa'],
        'Juguetes': ['Pelotas', 'Gimnasio para Gatos', 'otros']
    }
    tiposAlimentos = ['Gato', 'Perro', 'Hamster']
    nombresAlimentos = {
        'Gato': ['Mirringo', 'Gatsy'],
        'Perro': ['Ringo', 'NutreCan'],
        'Hamster': ['Semillas de girasol', 'Nueces']
    }
    nombresMascostas = ['Rocky', 'Loto', 'Rolita', 'Lucky']
    tiposProductos = ['Shampu', 'Crema', 'Polvo para pulgas']
    nombresProductos = {
        'Shampu': ['CanLove', 'Bolvo Shampu'],
        'Crema': ['Hidratante', 'Alisar pelaje'],
        'Polvo para Pulgas': ['Bolvo', 'Nexgard']
    }
    tiposMascotas=['Perros','Gatos','Hamsters']
    razasMascotas={
        'Perros':['Labrador','Pitbull','BullTerrier'],
        'Gatos':['Siames','Angora'],
        'Hamsters':['Ruso','Albino']
    }
    #ACCESORIO
    tipoAccesorio=random.choice(tiposAccesorios)
    nombreAccesorio=random.choice(nombresAccesorios[tipoAccesorio])
    accesorio=Accesorio(tipoAccesorio,nombreAccesorio)
    saver.guardar_accesorio(accesorio)
    Persistencia.save_json_accesorio(accesorio)
    #ALIMENTO
    tipoAlimento=random.choice(tiposAlimentos)
    nombreAlimento=random.choice(nombresAlimentos[tipoAlimento])
    alimento=AlimentoMascota(tipoAlimento,nombreAlimento)
    saver.guardar_alimento(alimento)
    Persistencia.save_json_alimento(alimento)
    #PELUQUERIA
    nombreMascota=random.choice(nombresMascostas)
    peluqueria=PeluqueriaCanina(nombreMascota)
    saver.guardar_peluqueria(peluqueria)
    Persistencia.save_json_peluqueria(peluqueria)
    #PRODUCTO
    tipoProducto=random.choice(tiposProductos)
    nombreProducto=random.choice(nombresProductos[tipoProducto])
    producto=ProductoAseoMascota(tipoProducto,nombreProducto)
    saver.guardar_producto(producto)
    Persistencia.save_json_producto(producto)
    #VENTA
    tipoMascota=random.choice(tiposMascotas)
    razaMascota=random.choice(razasMascotas[tipoMascota])
    venta=VentaMascota(tipoMascota,razaMascota)
    saver.guardar_venta(venta)
    Persistencia.save_json_venta(venta)

    inventario_json=Inventario()
    for file in os.listdir("./files"):
        if '.json' in file:
            inventario_json.agregar_accesorio(Persistencia.load_json_accesorio(file))
            inventario_json.agregar_alimento(Persistencia.load_json_alimento(file))
            inventario_json.agregar_peluqueria(Persistencia.load_json_peluqueria(file))
            inventario_json.agregar_producto((Persistencia.load_json_producto(file)))
            inventario_json.agregar_venta(Persistencia.load_json_venta(file))
