from unittest import TestCase, main

from core import ScannerOperations

valid_expresions = [
    "12 + 34.56 * 78 / 90",
    "-5.6 + 8 - 2.3 / 1.5",
    "100.5 - 20 * 3 + 6 / 2",
    "0.5 * 2 - 7 / 3",
    "15 + 3 - 1.5 * 2 / 4",
    "25.6 * 4 / 2 - 10 + 5.5",
    "-2.5 / 5 + 1.5 * 3 - 7",
    "50 - 10 / 2.5 * 4 + 5",
    "-1.25 * 8 / 0 + 5 - 3.75",
    "15 / 3 + 2 - 1 * 4"]

invalid_expresions = [
    "2 + 5 * (3 - 1)",
    "10 + 2 / ",
    "8.5 - / 2.3",
    "4 * (6 - 2) + 7 / 0",
    "12.5 + 3.2 * / 5",
    "20 / (4 - 2) + 6 * 2",
    "1.5 * (4 / 2) + -3",
    "9. - 6 / 0.5 * 2",
    "7 * (2 + 3 - 1))",
    "1.2 + 4 / (3 - 2)"]


class TestScanner(TestCase):

    def test_valid_expresions(self):
        for expresion in valid_expresions:
            scanner = ScannerOperations()
            assert scanner.scanner(string=expresion)

    def test_invalid_expresions(self):
        for expresion in invalid_expresions:
            scanner = ScannerOperations()
            assert not scanner.scanner(string=expresion)


if __name__ == '__main__':
    main()
