def teste():
    global mensagem
    mensagem = "Estou dentro da função"
    print(id(mensagem))
    print(mensagem)
    def funcao_aninhada():
        nonlocal x
        print("===========================")
        x = "Estou dentro da função interna"
        print(id(x))
    print("===========================")
    x =  "Estou fora da função interna"
    funcao_aninhada()
    print(x)
    print(id(x))

mensagem = "Estou fora da função"
print(id(mensagem))
print(mensagem)
print("===========================")
teste()
print("===========================")
print(id(mensagem))
print(mensagem)
