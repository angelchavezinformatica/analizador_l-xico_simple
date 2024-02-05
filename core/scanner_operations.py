import re

from typing import List

from core.scanner_number import ScannerNumber
from .errors import ScannerNumberInvalid, ScannerOperationsInvalid

ListStr = List[str]


class ScannerOperations:
    def __init__(self) -> None:
        self.operations = "+-*/"

    def scanner(self, string: str) -> None:
        scaner_number = ScannerNumber()
        state = 0

        try:
            for st in self._split_str(string=string):
                if state == 0:
                    scaner_number.scanner(st)
                    state = 1
                elif state == 1:
                    if (len(st) == 1) and (st in self.operations):
                        state = 0
                else:
                    raise ScannerOperationsInvalid()
        except ScannerNumberInvalid or ScannerOperationsInvalid:
            return False
        else:
            if state == 1:
                return True
        return False

    def _split_str(self, string: str) -> ListStr:
        return re.sub(pattern=r'\s+', repl=' ', string=string).split(" ")
