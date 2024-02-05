from .errors import ScannerNumberInvalid


class ScannerNumber:
    def __init__(self) -> None:
        self.numbers = "0123456789"

    def scanner(self, string: str) -> None:
        state = 0
        lenght = len(string)

        for i in range(lenght):
            char = string[i]

            if state == 0:
                if char in '+-':
                    state = 1
                elif char in self.numbers:
                    state = 2
                else:
                    raise ScannerNumberInvalid()
            elif state == 1:
                if char in self.numbers:
                    state = 2
                else:
                    raise ScannerNumberInvalid()
            elif state == 2:
                if char in self.numbers:
                    state = 2
                elif char == '.':
                    state = 3
                else:
                    raise ScannerNumberInvalid()
            elif state == 3:
                if char in self.numbers:
                    state = 4
                else:
                    raise ScannerNumberInvalid()
            elif state == 4:
                if char in self.numbers:
                    state = 4
                else:
                    raise ScannerNumberInvalid()
        else:
            if state in (2, 4):
                return
        raise ScannerNumberInvalid()
