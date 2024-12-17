# Exercício 7.3

from datetime import datetime

def main() -> None:
    with open("/home/tomm/Documents/University/IPRP/2024-11-12/primeiro.txt", "a") as ficheiro:
        ficheiro.write(f"\n{datetime.now().strftime("%d/%m/%Y")}")

if __name__ == '__main__':
    main()
