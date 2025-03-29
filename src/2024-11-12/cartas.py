# Exercício 7.15

from datetime import datetime

def limparLista(lista: list[str]) -> list[str]:
    lista.remove(lista[0])
    lista.remove(lista[-1])
    for i in range(len(lista)):
        lista[i] = lista[i].strip()
        lista[i] = lista[i].replace("\n", "")
        lista[i] = lista[i].replace('"', "")
        lista[i] = lista[i].replace(": {", "")
        lista[i] = lista[i].replace(",", "")
        lista[i] = lista[i].replace("nome: ", "")
        lista[i] = lista[i].replace("dia: ", "")
        lista[i] = lista[i].replace("mes: ", "")
        lista[i] = lista[i].replace("ano: ", "")
        lista[i] = lista[i].replace("morada: ", "")
        lista[i] = lista[i].replace("numeroTelefone: ", "")
    lista = [x for x in lista if x != '}' and x != "dataNascimento"]
    return lista

def criarDicionarioClientes(lista: list) -> dict:
    numeroClientes: list[int] = [int(x) for x in lista[::7]]
    
    informacaoClientes: dict = dict()
    for i in numeroClientes:
        cliente: list = lista[7 * (i - 1):7 * i]
        informacaoClientes.update({
            f"{cliente[0]}": {
                "nome": cliente[1],
                "dataNascimento": {
                    "dia": int(cliente[2]),
                    "mes": int(cliente[3]),
                    "ano": int(cliente[4])
                },
                "morada": cliente[5],
                "numeroTelefone": int(cliente[6])
            }
        })
    return informacaoClientes

def perguntarAno() -> int:
    try:
        ano: int = int(input("Insire o ano de referência: ").strip())
        return ano
    except ValueError:
        print("Insire um número natural.")
        return perguntarAno()

def selecionarValidos(clientes: dict, ano: int) -> dict:
    novoDicionario: dict = dict()
    for i in clientes:
        if clientes[i]["dataNascimento"]["ano"] < ano:
            novoDicionario.update({ f"{i}": clientes[i] })
    return novoDicionario

def escreverCartas(clientes: dict) -> None:
    #with open("/home/tomm/Documents/University/IPRP/2024-11-12/cartas")
    for cliente in clientes:
        texto: str = f"""{clientes[cliente]["morada"]}
{datetime.now().strftime("%d/%m/%Y")}

Caro/a {clientes[cliente]["nome"]},
Mando-lhe esta carta sem saber ao certo que escrever. Eu sei que isto deve parecer confuso, mas tenho uma explicação.
Esta carta não é nada mais que um exercício da minha cadeira de Introdução à Programação e Resolução de Problemas no curso de Engenharia Informática. O exercício consiste em pegar num ficheiro com informações de clientes duma certa empresa e enviar uma carta àqueles que nasceram antes de um dado ano. Se recebeu esta carta, parabéns! É um dos cotas qualificado a recebê-la.
Eu sei que ler isto pode dar crises existenciais, já que é meramente uma personagem de um exercício sem importância, mas sinceramente, eu não podia me importar menos. Deixo isso aos caloiros de Psicologia.
Além disso, como é apenas uma personagem criada por mim e que provavelmente vou me esquecer amanhã, nem sequer tem direito a terapia. Ou será que ao criá-lo acabei por criar um mundo onde todas as personagens que criei exitem, onde existem psicólogos? Deixo isto aos caloiros de Filosofia.
Espera que tenha um bom dia e que nunca se esqueça o quão inútil é a sua vida e até a próxima vez que me sinta nostálgico e que queira experimentar os meus programas antigos.

Cumprimentos,
Tomás Correia (o vosso Deus)"""

        with open(f"/home/tomm/Documents/University/IPRP/2024-11-12/cartas/{clientes[cliente]["nome"]}.txt", "w") as carta:
            carta.write(texto)

def main() -> None:
    clientes = open("/home/tomm/Documents/University/IPRP/2024-11-12/clientes.txt", "r")
    listaClientes: list[str] = clientes.readlines()
    listaClientes: list[str] = limparLista(listaClientes)
    listaClientes: dict = criarDicionarioClientes(listaClientes)
    anoReferencia: int = perguntarAno()
    clientesValidos: dict = selecionarValidos(listaClientes, anoReferencia)
    escreverCartas(clientesValidos)

if __name__ == '__main__':
    main()
