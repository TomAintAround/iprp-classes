# Exercício 4.20

def total(periodo, duracao):
    return int(1 / periodo * 525600 * duracao)

frequenciaNascimentos = int(input("Frequência de nascimentos (minutos): ").strip())
frequenciaMortes = int(input("Frequência de mortes (minutos): ").strip())
frequenciaEmigrantes = int(input("Frequência de emigração (minutos): ").strip())
populacaoInicial = int(input("População inicial: ").strip())
duracao = int(input("Duração (anos): ").strip())

nascimentos = total(frequenciaNascimentos, duracao)
mortes = total(frequenciaMortes, duracao)
emigrantes = total(frequenciaEmigrantes, duracao)

populacaoFinal = populacaoInicial + nascimentos - mortes - emigrantes

print("A estimativa da população final é {}.".format(populacaoFinal))