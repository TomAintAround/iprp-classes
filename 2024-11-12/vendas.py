# Exercício 7.11

from collections.abc import Callable

def perguntar(tipo, frase: str, erro: str, condicao: Callable[[], bool]):
    """Cria um input

    Args:
        tipo (_type_): Tipo da variável (int, float, str, ...)
        frase (str): Pergunta a ser feita
        erro (str): Frase que é imprimida quando existe um ValueError
        condicao (Callable[[], bool]): Condição que verifica a validez do número dado

    Raises:
        ValueError: Se o valor dado for incompatível com o tipo de variável ou a condição não for cumprida

    Returns:
        _type_: Valor do input
    """    
    try:
        valor = tipo(input(frase).strip())

        if condicao(valor):
            return valor
        else:
            raise ValueError
    except ValueError:
        print(erro)
        return perguntar(tipo, frase, erro, condicao)

def verificarFevereiro(dia: int, ano: int) -> bool:
    """Verifica se o dia dado é válido no mês de fevereiro, de acordo com o ano

    Args:
        dia (int): Dia
        ano (int): Ano

    Returns:
        bool: Validez do dia
    """    
    if ano % 4 == 0 and not ano % 100 == 0 or ano % 400 == 0:
        return dia <= 29
    else:
        return dia <= 28

def verificarDia(ano: int, mes: int, dia: int) -> bool:
    """Verifica se o dia dado é válido de acordo com o mês e ano

    Args:
        ano (int): Ano
        mes (int): Mês
        dia (int): Dia

    Returns:
        bool: Validez do dia
    """    
    if dia < 1 or dia > 31:
        return False
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return dia <= 31
    if mes in (4, 6, 9, 11):
        return dia <= 30
    else:
        return verificarFevereiro(dia, ano)
    
def selecionarMes(mes: int) -> str:
    """Transforma um número à abreviatura do respetivo mês

    Args:
        mes (int): Número do mês

    Returns:
        str: Abreviatura do mês
    """    
    numeroVendasMes: dict = {
        1: "Jan",
        2: "Fev",
        3: "Mar",
        4: "Abr",
        5: "Mai",
        6: "Jun",
        7: "Jul",
        8: "Ago",
        9: "Set",
        10: "Out",
        11: "Nov",
        12: "Dez"
    }
    return numeroVendasMes[mes]

def main() -> None:
    vendas: dict = {
        "empresa": perguntar(
            str, 
            "Insire o nome da empresa: ", 
            "", 
            lambda x: True
        ),
        "nc": perguntar(
            int, 
            "Insire o NC (número natural): ", 
            "Insire um número natural.", 
            lambda x: x > 0
        ),
        "ano": perguntar(
            int, 
            "Insire o ano da transação: ", 
            "Insire um número natural.", 
            lambda x: True
        ),
        "mes": perguntar(
            int, 
            "Insire o mês da transação: ", 
            "Insire um número entre 1 e 12.", 
            lambda x: x > 0 and x < 13
        ),
    }
    vendas.update({
        "dia": perguntar(
            int, 
            "Insire o dia da transação: ", 
            "Insire um dia válido.", 
            lambda dia: verificarDia(vendas["ano"], vendas["mes"], dia)
        ),
        "valor": perguntar(
            float, 
            "Insire o valor da transação (€, números positivos): ", 
            "Insire um número maior que 0.", 
            lambda x: x > 0
        ),
        "vendedor": perguntar(
            str, 
            "Insire o nome do vendedor: ", 
            "", 
            lambda x: True
        )
    })
    vendas["mes"] = selecionarMes(vendas["mes"])

    with open("/home/tomm/Documents/University/IPRP/2024-11-12/vendas.txt", "r") as ficheiro:
        numeroVendas: int = len(ficheiro.readlines())

    with open("/home/tomm/Documents/University/IPRP/2024-11-12/vendas.txt", "a") as ficheiro:
        ficheiro.write(f"{vendas}\n")

    print(f'''Venda a Dinheiro No {numeroVendas + 1}
----------------------------
Empresa: {vendas["empresa"]}
N.C.: {vendas["nc"]}
Data: {vendas["dia"]}/{vendas["mes"]}/{vendas["ano"]}
Valor: {vendas["valor"]}
Vendedor: {vendas["vendedor"]}''')

if __name__ == '__main__':
    main()
