import os
import json
from flask import request


class FileManager:
    @staticmethod
    def load_data(name):
        file_path = f"data/{name}.json"
        if not os.path.isfile(file_path):
            return []
        with open(f"data/{name}.json") as f:
            return json.loads(f.read())

    @staticmethod
    def save_data(name, data):
        with open(f"data/{name}.json", 'w') as f:
            return json.dump(data, f)

    @classmethod
    def add_item(cls, name):
        if not request.data:
            return False

        data = json.loads(request.data)
        item = data.get('item', False)

        if not item:
            return False

        items = cls.load_data(name)
        if item not in items:
            items.append(item)
        cls.save_data(name, items)

        return True

    @classmethod
    def rm_item(cls, name):
        if not request.data:
            return False

        data = json.loads(request.data)
        item = data.get('item', False)

        if not item:
            return False

        items = cls.load_data(name)
        items.remove(item)
        cls.save_data(name, items)

        return True
