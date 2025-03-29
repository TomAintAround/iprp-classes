def strsub(frase: str, remover: str) -> str:
	posicao: int = 0
	for letra in remover:
		if letra not in frase[posicao::]:
			break
		posicao += frase[posicao::].index(letra)
		frase = frase[:posicao:] + frase[posicao::].replace(letra, "", 1)
	return frase

def main() -> None:
	print(strsub("pergunta que parece descabida", "aaa"))
	print(strsub("pergunta que parece descabida", "grecia"))
	print(strsub("pergunta que parece descabida", "austria"))

if __name__ == "__main__":
	main()