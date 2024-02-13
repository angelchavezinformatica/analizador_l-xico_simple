import re

from core.scanner_number import ScannerNumber
from .errors import ScannerNumberInvalid, ScannerOperationsInvalid


class ScannerOperations:
    def __init__(self) -> None:
        self.operators = "+-*/"

    def scanner(self, string: str):
        scaner_number = ScannerNumber()
        state = 0

        try:
            for token in self._split_str(string=string):
                if state == 0:
                    scaner_number.scanner(string=token)
                    state = 1
                elif state == 1 and token in self.operators:
                    state = 0
                else:
                    raise ScannerOperationsInvalid()
                yield token
        except ScannerNumberInvalid:
            raise ScannerOperationsInvalid()
        if state == 1:
            return
        raise ScannerOperationsInvalid()

    def _split_str(self, string: str):
        tokens = re.sub(pattern=r'\s+', repl=' ',
                        string=string).strip().split(" ")
        for token in tokens:
            yield token
