from inventory_report.inventory.inventory import Inventory
import sys


def main():
    try:
        path = sys.argv[1]
        type = sys.argv[2]
        inventory_report = Inventory()
        print(inventory_report.import_data(path, type), end="")
    except IndexError:
        print("Verifique os argumentos", file=sys.stderr)
