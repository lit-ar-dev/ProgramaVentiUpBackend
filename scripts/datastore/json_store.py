import json
import os
from scripts.datastore.base import DataStoreInterface


class JSONDataStore(DataStoreInterface):
    def __init__(self, base_dir: str = "json"):
        self.base_dir: str = base_dir
        self.data: dict = {}
        self._load_resources()

    def _load_resources(self):
        """Carga todos los archivos JSON en el directorio base."""
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)
        for filename in os.listdir(self.base_dir):
            if filename.endswith(".json"):
                resource: str = filename[:-5]  # Elimina la extensión '.json' para obtener el nombre del recurso
                file_path: str = os.path.join(self.base_dir, filename)
                with open(file_path, "r", encoding="utf-8") as f:
                    self.data[resource] = json.load(f)
            else:
                # Si no existe el archivo, inicializamos con una lista vacía
                self.data[resource] = []

    def _save_resource(self, resource: str):
        """Guarda en el archivo JSON los datos actualizados del recurso."""
        file_path: str = os.path.join(self.base_dir, f"{resource}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(self.data[resource], f, indent=4, ensure_ascii=False)

    def get_all(self, resource: str):
        return self.data.get(resource, [])

    def get(self, resource: str, id: dict):
        items: list[dict] = self.data.get(resource, [])
        id_field, id = next(iter(id.items()))
        for item in items:
            if int(item.get(id_field)) == id:
                return item
        return None

    def add(self, resource: str, data: dict):
        items: list[dict] = self.data.get(resource, [])
        new_id = max(item.get("id", 0) for item in items) + 1 if items else 1
        data["id"] = new_id
        items.append(data)
        self.data[resource] = items
        self._save_resource(resource)
        return data

    def update(self, resource: str, id: dict, new_data: dict):
        items: list[dict] = self.data.get(resource, [])
        id_field, id = next(iter(id.items()))
        for item in items:
            if int(item.get(id_field)) == id:
                item.update(new_data)
                self._save_resource(resource)
                return item
        return None

    def delete(self, resource: str, id: dict):
        items: list[dict] = self.data.get(resource, [])
        id_field, id = next(iter(id.items()))
        for index, item in enumerate(items):
            if int(item.get(id_field)) == id:
                del items[index]
                self._save_resource(resource)
                return True
        return False