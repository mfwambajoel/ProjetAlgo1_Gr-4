from time import time
from random import randint
from implementation1_module import *

print("Calcul du temps de la premiere implementation")
print()

liste_obj=[]

for i in range(1,101):
    fig=randint(1,3)
    if fig==1:
        lon=randint(50,120)
        larg=randint(45,90)
        objet=Rectangle(lon,larg)

    elif fig==2:
        rayon=randint(5,150)
        objet=Cercle(rayon)

    
    liste_obj.append(objet)

    print()
  
    liste_temps=[]

    for j in range(1,len(liste_obj)):
        temps=0

        for z in range(1,61):
            T_p=time()
            for element in range(0,j):
                objet=liste_obj[element]
                objet.surface()
                objet.perimeter
            T_off=time()
            Dtemps=T_off-T_p
            temps=temps/60
            liste_temps.append(temps)

#Execution du programme

fichier=open("infos_enreg.xls",w)

for temps in liste_temps:
    fichier.write(str(temps)+"\n")

fichier.close()


