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
    if key == 'Superman':
        for key_sup,value_sup in value.items():
            if key_sup == 'location':
                for key_loc,value_loc in value_sup.items():
                    if key_loc == 'city':
                        print(value_loc)
            
            
