from sys import exit

# Chama-se ano bissexto o ano ao qual é acrescentado um dia extra, 
# ficando com 366 dias, um dia a mais do que os anos normais de 365 dias, 
# ocorrendo a cada quatro anos (exceto anos múltiplos de 100 que não são 
# múltiplos de 400)[1].

def is_leap_year(year):
    ## Escreva seu teste aqui!!
    # Deve retornar True se for ano bissexto e False caso contrário
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def die(i):
    print(f"Seu programa está errado!  -->{i}")
    exit(1)

anos_bissextos = [2020, 2004, 1996, 1600, 2000, 2400, 2000, 2400]
anos_nao_bissextos = [ 1900, 2100, 2200, 2019, 2021, 1999]

if __name__ == "__main__":
    for i in anos_bissextos:
        if not is_leap_year(i):
            die(i)
            
    for i in anos_nao_bissextos:
        if is_leap_year(i):
            die(i)

    print("Seu programa está certo!")
