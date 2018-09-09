def somar(n1, n2):
    """Realiza a soma de dois números"""
    print("{n1} + {n2} = {result}".format(n1=n1, n2=n2, result=n1+n2))

def subtrair(n1, n2):
    """Realiza a subtração de dois números"""
    return n1 - n2

def multiplicar(n1, n2):
    """Realiza a multiplicação de dois números"""
    return n1 * n2

def dividir(n1, n2):
    """Realiaza a divisão de dois números , retornando o quociente e o resto"""
    return(n1 // n2, n1 % n2)

def media_aritimetica(*numbers):
    """Calcula a média aritimética dos números informados"""
    return sum(numbers) / len(numbers)
