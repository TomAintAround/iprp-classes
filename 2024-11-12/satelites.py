def obter_info(satelites: list) -> dict:
	dicionario: dict = dict()
	for linha in satelites:
		linha = linha.replace("\n", "")
		separados1: list = linha.split(":")
		nomeSatelite: str = separados1[0]
		atributos: str = separados1[1].split(",")
		dicionario[nomeSatelite] = dict()

		for atributo in atributos:
			separados2: list = atributo.split(" ")
			dicionario[nomeSatelite][separados2[0]] = separados2[1]

	return dicionario

def main() -> None:
	dicionario: dict = dict()
	with open("/home/tomm/Documents/University/IPRP/2024-11-12/satelites.txt", "r") as satelites:
		dicionario: dict = obter_info(satelites.readlines())
	print(dicionario)

if __name__ == "__main__":
	main()