import csv
import json
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport
from xmltodict import parse


def generate_file_by_end(type, input):
    if type == "simples":
        return SimpleReport.generate(input)
    elif type == "completo":
        return CompleteReport.generate(input)


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        with open(path, 'r') as file:
            input = []
            if path.endswith(".csv"):
                content = csv.DictReader(file, delimiter=",", quotechar='"')
            elif path.endswith(".json"):
                content = json.load(file)
            elif path.endswith(".xml"):
                xml_file = file.read()
                content = parse(xml_file)['dataset']["record"]
            for job in content:
                input.append(job)
        return generate_file_by_end(type, input)
