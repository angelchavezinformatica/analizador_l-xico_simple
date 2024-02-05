from core import ScannerOperations

if __name__ == '__main__':
    scanner = ScannerOperations()
    while True:
        inpt = input("Ingrese una expresión o enter: ")
        if inpt == "":
            break
        if scanner.scanner(string=inpt):
            print("Expresión válida")
        else:
            print("Expresión inválida")
