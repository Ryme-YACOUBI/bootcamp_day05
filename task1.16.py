liste=[1,1,1,1,2,2,3,4]
liste_sd=[]
k=0
for i in liste:
    if i not in liste_sd:
        liste_sd.insert(k,i)
        k += 1
print(liste_sd)