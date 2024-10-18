# Exercício 5.18

import turtle

numeroInvalido = -1

def gerarPergunta(pergunta, valor, tipo):
    if valor <= 0:
        valor = tipo(input(pergunta).strip())
        return gerarPergunta(pergunta, valor, tipo)
    else:
        return valor

def configurarCelulas(medidaTabela, numeroOcurrencias, dimensao):
    pergunta = lambda numero: gerarPergunta('{0} da célula {1} (%): '.format(dimensao, numero), numeroInvalido, eval)
    listaPercentagem = list(map(pergunta, range(1, numeroOcurrencias + 1)))
    somaPercentagem = sum(listaPercentagem)

    if somaPercentagem != 100:
        configurarCelulas(medidaTabela, numeroOcurrencias, dimensao)
    else:
        return list(map(lambda numero: numero * medidaTabela / 100, listaPercentagem))

def desenharTabela(alturaTabela, comprimentoTabela, alturaCelulas, comprimentoCelulas, espacoCabecalho):
    turtle.hideturtle()
    turtle.right(90)

    def borda(altura, comprimento, repeticoes):
        if repeticoes > 0:
            turtle.forward(altura)
            turtle.left(90)
            turtle.forward(comprimento)
            turtle.left(90)
            borda(altura, comprimento, repeticoes - 1)
    
    def linhas(comprimentoTabela, alturaCelulas, progresso):
        if progresso < len(alturaCelulas) - 1:
            turtle.forward(alturaCelulas[progresso])
            turtle.left(90)
            turtle.forward(comprimentoTabela)
            turtle.left(180)
            turtle.forward(comprimentoTabela)
            turtle.left(90)
            linhas(comprimentoTabela, alturaCelulas, progresso + 1)
        else:
            turtle.forward(alturaCelulas[progresso])
            turtle.left(90)
    
    def colunas(alturaTabela, alturaCelulas, comprimentoCelulas, espacoCabecalho, progresso):
        if progresso < len(comprimentoCelulas) - 1:
            turtle.forward(comprimentoCelulas[progresso])
            turtle.left(90)
            turtle.forward(alturaTabela - alturaCelulas[0])
            turtle.penup()
            turtle.forward(espacoCabecalho)
            turtle.pendown()
            turtle.forward(alturaCelulas[0])
            turtle.left(180)
            turtle.penup()
            turtle.forward(alturaTabela + espacoCabecalho)
            turtle.left(90)
            turtle.pendown()
            colunas(alturaTabela, alturaCelulas, comprimentoCelulas, espacoCabecalho, progresso + 1)
            
    repeticoes = 2
    comecoDaLista = 0
    
    borda(alturaCelulas[0], comprimentoTabela, repeticoes)
    turtle.penup()
    turtle.forward(alturaCelulas[0] + espacoCabecalho)
    turtle.pendown()
    borda(alturaTabela - alturaCelulas[0], comprimentoTabela, repeticoes)
    linhas(comprimentoTabela, alturaCelulas, comecoDaLista + 1)
    colunas(alturaTabela, alturaCelulas, comprimentoCelulas, espacoCabecalho, comecoDaLista)

    turtle.exitonclick()

alturaTabela = gerarPergunta('Altura da tabela: ', numeroInvalido, eval)
comprimentoTabela = gerarPergunta('Comprimento da tabela: ', numeroInvalido, eval)
numeroLinhas = gerarPergunta('Número de linhas: ', numeroInvalido, int)
numeroColunas = gerarPergunta('Número de colunas: ', numeroInvalido, int)
espacoCabecalho = gerarPergunta('Espaço entre o cabeçalho e as linhas: ', numeroInvalido, eval)
alturaCelulas = configurarCelulas(alturaTabela, numeroLinhas, 'Altura')
comprimentoCelulas = configurarCelulas(comprimentoTabela, numeroColunas, 'Comprimento')

desenharTabela(alturaTabela, comprimentoTabela, alturaCelulas, comprimentoCelulas, espacoCabecalho)