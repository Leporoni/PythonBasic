#import funcoes_aritimeticas as arit
from matematica.funcoes_aritimeticas import somar, subtrair, multiplicar, dividir, media_aritimetica

num1 = int(input("Digite um número: "))
action = input("Digite a operação desejada: ")
num2 = int(input("Digite outro número: "))

if action == "+":
    somar(num1, num2)
    print(somar.__doc__)
elif action == "-":
    result = subtrair(num1, num2)
    print("{n1} - {n2} = {result}".format(n1=num1, n2=num2, result=result))
elif action == "*":
    print("{n1} * {n2} = {result}".format(n1=num1, n2=num2, result=multiplicar(num1, num2)))
elif action == "/":
    quociente, resto = dividir(num1, num2)
    print("O quociente é ", quociente, " e o resto é " ,resto)

print("Média aritimética = {m}".format(m=media_aritimetica(10, 20, 30, 40)))
numbers = [50, 40, 30]
print("Outra média aritimética = {m}".format(m=media_aritimetica(*numbers)))