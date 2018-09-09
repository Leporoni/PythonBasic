warriors = ["Ninja", "Samurai", "Shinobi", "Musashi"]

wepons = ("shuriken", "katana", "kusarigama", "nunchako")

armaduras = [["azul", "amarela"], ["preta", "vermelha"]]

print(armaduras[1][0])
print(len(warriors))
warriors.append("Haomaru")
print(warriors)
slice_1 = wepons[1:3]
print(slice_1)
slice_2 = armaduras[-1]
print(slice_2)

print(armaduras * 2)

warriors.insert(2, "Hatori")
print(warriors)

warriors.pop()
print(warriors)
warriors.pop(3)
print(warriors)

warriors.extend(["Rygar", "Vastar", "Ryu", "Ken", "ChungLi"])
print(warriors)

print("Rygar" in warriors)
print("Zatoichi" in warriors)

indice_Rygar = warriors.index("Rygar", 1, 5) #filtrar por slice a busca
print(indice_Rygar)
indice_Ryu = warriors.index("Ryu")
print(indice_Ryu)