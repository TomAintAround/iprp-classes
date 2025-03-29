def compactarMatriz(matriz: list[list]) -> dict:
	matrizCompacta: dict = dict()
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			if matriz[i][j] != 0:
				matrizCompacta[(i + 1, j + 1)] = matriz[i][j]
	matrizCompacta["shape"]= (len(matriz), len(matriz[1]))
	return matrizCompacta

def main() -> None:
	print(compactarMatriz([[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0], [3, 4, 0, 0]]))
	print(compactarMatriz([[1, 0], [0, 0], [0, 9], [3, 4]]))

if __name__ == "__main__":
	main()