from .importer import Importer
import json


class JsonImporter(Importer):

    @classmethod
    def import_data(cls, path):
        with open(path, 'r') as file:
            output = []
            if path.endswith(".json"):
                content = json.load(file)
            else:
                raise ValueError("Arquivo inválido")
            for job in content:
                output.append(job)
        return output
