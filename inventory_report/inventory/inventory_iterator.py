from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data) -> None:
        self.data = data
        self.iterator = 0

    def __next__(self):
        try:
            output = self.data[self.iterator]
            self.iterator += 1
            return output
        except IndexError as error:
            return error
