superheroes = {
"Batman" : {
"id": 1,
"aliases": ["Bruce Wayne", "Dark knight"],
"location": {
"number" : 1007,
"street": "Mountain Drive",
"city": "Gotham"
}
},
"Superman" : {
"id": 2,
"aliases": ["Kal-El", "Clark Kent", "The Man of Steel"],
"location": {
"number" : 344,
"street": "Clinton Street",
"apartment": "3D",
"city": "Metropolis"
}
},
}
for key,value in superheroes.items():
    if key=='Batman':
        for key_bat,value_bat in value.items():
            if key_bat=='aliases':
                value_bat.append("Caped Crusader")
superheroes['Wolverine'] = {"id" : 3, "aliases":[],"location":{}}
print(superheroes)