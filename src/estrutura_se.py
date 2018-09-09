idade = int(input("Qual a sua idade? "))

if idade < 18:
    print("Você é de menor!!!")
else:
    print("Você é de maior!!!")
if idade < 18:
    print("Você é uma criança!!!")
elif idade >= 18 and idade <= 65:
    print("Você é um adulto!!!")
else:
    print("Você é um idoso!!!")