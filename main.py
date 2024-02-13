from core import ScannerOperations, ScannerOperationsInvalid

if __name__ == '__main__':
    scanner = ScannerOperations()

    while True:
        inpt = input("Ingrese una expresión o enter: ")

        if inpt == "":
            break

        try:
            for _ in scanner.scanner(string=inpt):
                pass
        except ScannerOperationsInvalid:
            print("Expresión inválida")
            continue
        print("Expresión válida")
