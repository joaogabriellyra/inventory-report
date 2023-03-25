from inventory_report.inventory.inventory import Inventory
import sys


def main():
    try:
        path = sys.argv[1]
        type = sys.argv[2]
        inventory_report = Inventory()
        print(inventory_report.import_data(path, type))
    except IndexError as err:
        err = "Verifique os argumentos\n"
        return err
