liste=["Ryme",2,"Epitech",9,10,"Pomme"]
liste_tmp=[]
for i in range(len(liste)-1,-1,-1):
    liste_tmp.insert(len(liste)-i+1,liste[i])
print(liste_tmp)
