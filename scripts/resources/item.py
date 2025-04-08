from flask import request, jsonify
from flask_restful import Resource
from ..utils.config import data_store


class ItemResource(Resource):
    """Maneja operaciones sobre un ítem (GET, PUT, DELETE) de una colección."""
    def __init__(self, resource_name, id_field="id"):
        self.resource_name: str = resource_name
        self.id_field: str = id_field

    def get(self, id):
        item = data_store.get(self.resource_name, {self.id_field: id})
        if not item:
            return {"mensaje": f"{self.resource_name[:-1].capitalize()} no encontrado"}, 404
        return jsonify(item)

    def put(self, id):
        data = request.get_json()
        updated_item = data_store.update(self.resource_name, {self.id_field: id}, data)
        if not updated_item:
            return {"mensaje": f"{self.resource_name[:-1].capitalize()} no encontrado"}, 404
        return jsonify(updated_item)

    def delete(self, id):
        success = data_store.delete(self.resource_name, {self.id_field: id})
        if not success:
            return {"mensaje": f"{self.resource_name[:-1].capitalize()} no encontrado"}, 404
        return {"mensaje": f"{self.resource_name[:-1].capitalize()} eliminado correctamente"}, 200