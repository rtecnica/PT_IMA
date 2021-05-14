import web
import json
from pymongo import MongoClient
from bson.objectid import ObjectId
import requests
from datetime import datetime
from threading import Thread

# String de conección a Atlas MongoDB
connect_str = 'mongodb+srv://rtecnica:EskriR4DXFwk9J90@cluster0.qbrqm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

# Importar plantilla de controlador de API Rest
from restful_controller import RESTfulController

# Patrón para manejo de URLs
urls = (
    r'/payloads(?:/(?P<payload_id>(?:[0-9]|[A-z])+))?',
    'PayloadController',
)

# Declaro variable global para conección a MongoDB
client = MongoClient(connect_str)

# Clase para API Rest, hereda de plantilla de comportamientos genéricos
class PayloadController(RESTfulController):

    # Listar cuando GET no especifica ID
    def list(self):
        strlist = ""
        for resource in client.Test.Test.find():
            strlist = strlist + str(resource) + "\n"
        return strlist

    # Método GET
    def get(self, payload_id):
        return client.Test.Test.find_one({"_id": ObjectId(str(payload_id))})

    # Método POST
    def create(self):
        payload = json.loads(web.data())
        if client.Test.Test.find_one(payload) is None:
            post_id = client.Test.Test.insert_one(payload).inserted_id
            return "Document inserted with ID:", post_id
        else:
            return "Identical Document exists! Please use UPDATE"

    # Método PUT - sin implementar
    def update(self, payload_id):
        return "updated resource", payload_id

    # Método DELETE - sin implementar
    def delete(self, payload_id):
        return "deleted resource", payload_id


def main():
    # Abrir archivo con payloads en texto plano
    with open("payload", "r") as ah_file:
        data = ah_file.readlines()

    # Variables de utilidad
    payloads = []
    tempstr = ""

    # Traspasar payloads a strings unicos
    for line in data:
        # Separar Payloads por linea vacía
        if line == '\n':
            payloads.append(tempstr)
            tempstr = ""
        else:
            # Limpiar newlines y convertir a ASCII
            tempstr = tempstr + bytes.fromhex(line.replace('\n', '')).decode()

    # Convertir strings a JSON, agregando estampa de tiempo
    for p in range(len(payloads)):
        payloads[p] = json.loads("{" + payloads[p].replace('=>', ':') + "}")
        payloads[p]["time"] = str(datetime.utcnow())

    # Subir payloads a MongoDB, usando API
    db = client.Test
    collection = db.Test
    for p in range(len(payloads)):
        if collection.find_one(payloads[p]) is None:
            r = requests.post('http://localhost:8080/payloads', data=str(payloads[p]).replace("\'", "\""))


if __name__ == "__main__":
    # Iniciar Servidor
    app = web.application(urls, globals())
    Thread(target=app.run).start()
    # Iniciar Aplicación
    main()
