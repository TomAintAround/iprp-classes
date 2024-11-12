def digito_valido(cnpj, pesos, digito):
    count = 0
    progress = 0
    for numero in pesos:
        mul = int(cnpj[progress]) * numero
        progress += 1
        count += mul
    resto = count % 11

    if resto < 2:
        if int(cnpj[digito]) != 0:
            return False
    else:
        if int(cnpj[digito]) != 11 - resto:
            return False

def valida_cnpj(cnpj):
    if len(cnpj) != 14 or not cnpj.isalnum():
        print(False)
        return

    pesos1 = (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
    pesos2 = (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
    if digito_valido(cnpj, pesos1, -2) is False or digito_valido(cnpj, pesos2, -1) is False:
        print(False)
        return
    
    print(True)
    return

valida_cnpj("11222333000100")
