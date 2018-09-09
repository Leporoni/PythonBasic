import sys

class NumeroCaracteresMenorQueTresError(Exception):
    pass

nomes = {"Andresa":1981, "Amelia":1946, "Alex":1975, "Geraldo":1930, "Nello":1913}
try:
    nome = input("Entre com o nome da pessoa para saber a data de nascimento: ")
    if len(nome) < 3:
        raise NumeroCaracteresMenorQueTresError("O nome deve ter mais do que três caracteres!!!")
    birthday = nomes[nome]
    print(nome, "nasceu no ano de",birthday)
except (KeyError, NumeroCaracteresMenorQueTresError):
    print("O nome da pessoa não existe no dicionario ou o numero de caracteres é insuficiente para a pesquisa")
except:
    print("O nome digitado não existe na lista, tente novamente")
finally:
    print("Obrigado por usar o nosso sistema!!!")