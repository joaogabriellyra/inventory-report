from collections.abc import Iterable
from .inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, type):
        if (len(self.data) == 0):
            self.data = self.importer.import_data(path)
        else:
            self.data += self.importer.import_data(path)
