names = { "Miyamoto" : "Musashi", "Joe" : "Higashi", "Masaaki" : "Hatsume"}
print(names)
print("Joe " + names["Joe"])

print("Miyamoto" in names)
print("Higashi" in names)

del names["Joe"]
print(names)

names["Alex"] = "Leporoni"
print(names)

last_name = names.pop("Alex")
print(last_name)
print(names)

more_names = {"Amelia" : "Leporoni", "Andresa" : "DePaula"}
names.update(more_names)
print(names)