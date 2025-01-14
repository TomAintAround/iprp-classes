def obter_info(satelites: list) -> dict:
	dicionario: dict = dict()
	for linha in satelites:
		linha = linha.replace("\n", "")
		nomeSatelite: str = linha[:2:]
		dicionario[nomeSatelite] = dict()
		atributos: list = linha[3::].split(",")

		for atributo in atributos:
			separados: list = atributo.split(" ")
			dicionario[nomeSatelite][separados[0]] = separados[1]

	return dicionario

def main() -> None:
	dicionario: dict = dict()
	with open("/home/tomm/Documents/University/IPRP/2024-11-12/satelites.txt", "r") as satelites:
		dicionario: dict = obter_info(satelites.readlines())
	print(dicionario)

if __name__ == "__main__":
	main()