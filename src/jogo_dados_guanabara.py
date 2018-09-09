from random import randint
from time import sleep
from operator import itemgetter
game = {"Player1":randint(1, 6), "Player2":randint(1,6), "Player3":randint(1,6), "Player4":randint(1,6)}
ranking = list()
print("Sorted Values")
for k, v in game.items():
    print(f'{k} tirou {v} no dado!')
    sleep(1)
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print(' == Players Ranking == ')
for i, v in enumerate(ranking):
    print(f' {i+1}º place: {v[0]} with:{v[1]}')
    sleep(1)
print('-=' * 30)
