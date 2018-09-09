teste = input("Digite um nome: ") # O usuário entrará com "AB"
try:
  if len(teste) < 3:
    raise ValueError("Ops!")
finally:
  print("Finalizei por aqui.")