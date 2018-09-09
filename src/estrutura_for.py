numero = int(input("Digite um número: "))
for i in range(11):
    print( "{n} x {i} = {resultado}".format(n=numero, i=i, resultado=numero*i))
else:
    print("**Processo Concluído**")

linguagens = ["Python", "Java", "C#", "Node", "Go"]
print("Algumas linguagens de programação são: ")
for linguagem in linguagens:
    print(" - " + linguagem)

capitais = {"SP":"São Paulo", "MG":"Belo Horizonte", "RJ":"Rio de Janeiro"}
print("Algumas capitais: ")
for sigla, capital in capitais.items():
    print(" - {sigla}: {capital}".format(sigla=sigla, capital=capital))

