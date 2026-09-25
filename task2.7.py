types = {'Electric': ['Pikachu'], 'Grass': ['Bulbasaur', 'Leafeon', 'Scovillain'], 'Fire': ['Scovillain', 'Charmander'], 'poison': ['Bulbasaur']}
for i in types:
    if 'Pikachu' in types[i]:
        print(i)
for key, value in types.items():
    if 'Pikachu' in value:
        print(key)