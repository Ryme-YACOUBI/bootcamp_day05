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
    print(f"{key} :")
    for key_sup,value_sup in value.items():
        if key_sup=='aliases':
            for i in value_sup:
                print(i)
            print("\n")