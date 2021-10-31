import json
import waitress
import falcon
from falcon import API

from TiendaMaquillaje.Infraestructura.Persistencia import Persistencia
import uuid


class Prueba():
    def on_get(self, req,resp, codigo):
        db = Persistencia()
        producto = db.load_json_perfume(codigo + '.jsonPerfume')
        resp.body = json.dumps(producto.__dict__)
        resp.status = falcon.HTTP_OK


def iniciar() -> API:
    api = API()
    api.add_route("/perfume/{codigo}", Prueba())

    return api


app = iniciar()

if __name__ == '__main__':
    waitress.serve(app, port=5050, url_scheme='http')
#     def on_get(self, resp, uuid):
#         db = Persistencia()
#         producto = db.load_json_perfume(str(uuid) + '.json')
#         resp.body = json.dumps(producto.__dict__)
#         resp.status = falcon.HTTP_OK
#
#
# def iniciar() -> API:
#     api = API()
#     api.add_route("/perfume/{uuid}", TiendaMaquillaje())
#     return api
#
#
# app = iniciar()
#
# if __name__ == '__main__':
#     waitress.serve(app, port=2020, url_scheme='http')
