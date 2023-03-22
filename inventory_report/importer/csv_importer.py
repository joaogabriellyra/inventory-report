from .importer import Importer
import csv


class CsvImporter(Importer):

    @classmethod
    def import_data(cls, path):
        with open(path, 'r') as file:
            output = []
            if path.endswith(".csv"):
                content = csv.DictReader(file, delimiter=",", quotechar='"')
            else:
                raise ValueError("Arquivo inválido")
            for job in content:
                output.append(job)
        return output
