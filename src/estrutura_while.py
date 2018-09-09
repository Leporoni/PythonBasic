amigos = []
nomes = ""

while nomes != "parar":
    nomes = input("Digite o nome de um amigo: ")
    if nomes != "parar":
        amigos.append(nomes)
else:
    print("**Fim dos Nomes dos Amigos**")
print("Seus amigos são: ")
print(amigos)

