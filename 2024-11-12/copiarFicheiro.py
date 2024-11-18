# Exercício 7.6

def copiaFicheiro(original, copia, destino):
    with open(f"{destino}/{original}", 'r') as ficheiro:
        texto: str = ficheiro.read()
    
    with open(f"{destino}/{copia}", 'w') as ficheiro:
        ficheiro.write(texto)

def main() -> None:
    original: str = input("Insire o nome do fichero original: ").strip()
    copia: str = input("Insire o destino do ficheiro cópia: ").strip()
    destino: str = "/home/tomm/Documents/University/IPRP/2024-11-12"

    copiaFicheiro(original, copia, destino)

if __name__ == '__main__':
    main()