liste=[42,'42', 42.0, 21+21, 42*10/10]
liste_sd=[]
k=0
for i in liste:
    if i not in liste_sd:
        liste_sd.insert(k,i)
        k += 1
print(liste_sd)
