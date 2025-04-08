from flask import request, jsonify
from flask_restful import Resource
from ..utils.config import data_store


class CollectionResource(Resource):
    """Maneja operaciones sobre colecciones (GET todos, POST nuevo item)."""
    def __init__(self, resource_name):
        self.resource_name = resource_name

    def get(self):
        items = data_store.get_all(self.resource_name)
        return jsonify(items)

    def post(self):
        data = request.get_json()
        new_item = data_store.add(self.resource_name, data)
        response = jsonify(new_item)
        response.status_code = 201
        return response