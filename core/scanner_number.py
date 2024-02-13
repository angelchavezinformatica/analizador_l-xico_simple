from .errors import ScannerNumberInvalid


class ScannerNumber:
    def __init__(self) -> None:
        self.numbers = "0123456789"
        self.signs = '+-'
        self.dot = '.'

    def scanner(self, string: str) -> None:
        state = 0

        for char in string:
            if state == 0 and char in self.signs:
                state = 1
            elif state == 0 and char in self.numbers:
                state = 2
            elif state == 1 and char in self.numbers:
                state = 2
            elif state == 2 and char in self.numbers:
                continue
            elif state == 2 and char in self.dot:
                state = 3
            elif state == 3 and char in self.numbers:
                state = 4
            elif state == 4 and char in self.numbers:
                continue
            else:
                raise ScannerNumberInvalid()
        if not (state == 2 or state == 4):
            raise ScannerNumberInvalid()
