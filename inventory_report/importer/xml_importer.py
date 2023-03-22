from .importer import Importer
from xmltodict import parse


class XmlImporter(Importer):

    @classmethod
    def import_data(cls, path):
        with open(path, 'r') as file:
            output = []
            if path.endswith(".xml"):
                xml_file = file.read()
                content = parse(xml_file)['dataset']["record"]
            else:
                raise ValueError("Arquivo inválido")
            for job in content:
                output.append(job)
        return output
