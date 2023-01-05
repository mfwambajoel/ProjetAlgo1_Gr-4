from implementation1_module import*

#Batterie des tests

#Pour exploiter le module , il suffit de faire cet appel

class Test():
    """classe pour tester le module importe"""
    try:
         print("Choisisser une figure pour le calcul de sa surface et du perimetre:\n 0. Triangle\n 1. Rectangle \n 2. Cercle \n 3. Triangle rectangle \n 4.Carre")
         print()
         for i in range (0,5):
             i=int(input("Choisissez l'option desire>>>"))
             print()
             if i==0:
                 text="0. Triangle"
                
                 print(text.center(75))
                 print()
                 c1=float(input("Entrer la valeur du premier cote>>>"))
                 c2=float(input("Entrer la valeur du deuxieme cote>>>"))
                 c3=float(input("Entrer la valeur du troisieme cote>>>"))
                 Tri=Triangle(c1,c2,c3)
                 Tri.mesures()
                 print()
             if i==1:
                text="1. Rectangle"
                print(text.center(75))
                print()
                lon=float(input("Entrer la valeur de la longueur du rectange>>>"))
                larg=float(input("Entrer la valeur de la largeur>>>"))
                Rec=Rectangle(lon,larg)
                Rec.mesures()

             if i==2:
                 text="2. Cercle"
                
                 print(text.center(75))
                 print()
                 Rayon=float(input("Entrer la valeur du rayon du cercle>>>"))
                 Cer=Cercle(Rayon)
                 Cer.mesures()
                 print()
             if i==3:
                 text="3. Triangle rectangle"
                 print(text.center(75))
                 print()

                 C1=float(input("Entrer la valeur du cote adjacent>>>"))
                 C2=float(input("Entrer la valeur du cote oppose>>>"))
                 TriR=TriRectangle(C1,C2)
                 TriR.mesures()
                 print()
             if i==4:
                 text="4. Carre"
                 print(text.center(75))

                 Cote=float(input("Entrer le cote du carre>>>"))
                 Car=Carre(Cote)
                 Car.mesures()

    except:
        print("Entrees incorrectes")






