#Deuxieme implementation sans utiliser l'heritage

from math import*


class GeomForm:
    """Classe de base"""

    def __init__(self):
        self._surf=None
        self._perim=None

    
    def getsurf(self):

        return self._surf

    def getperim(self):
        return self._perim

#Au lieu de definir les classes, nous definissons 
#les methodes


    def rectangle(self,lon,larg):
        self._lon=lon
        self._larg=larg
        self._nom="Rectangle"
        self._surf=self._lon*self._larg
        self._perim=2*(self._larg+self._lon)
        return " Le {} a une surface {} et un perimetre de {}".format(self._nom,self._surf,self._perim)

    def cercle(self,rayon):
        self._rayon=rayon
        self._surf=pi*self._rayon*self._rayon
        self._perim=2*pi*self._rayon
        self._nom="cercle"
        return " Le {} a une surface {} et un perimetre de {}".format(self._nom,self._surf,self._perim)

    def triangle(self,coteA,coteB,coteC):
        self._coteA=coteA
        self._coteB=coteB
        self._coteC=coteC
        self._nom="triangle"
        p= self._coteA + self._coteB + self._coteC
        s= abs(p * (p - self._coteA) * (p - self._coteB) * (p - self._coteC))
        self._surf=sqrt(s)
        self._perim=p
        return " Le {} a une surface {} et un perimetre de {}".format(self._nom,self._surf,self._perim)
                                                                      

class Test():
   try:
       print("Choisissez l'option convenable \n 0.Rectangle \n 1.Cercle \n 2.Triangle")
       for i in range(0,3):
           i=int(input("Choisissez l'option:"))
           if i==0:
               lon=float(input("Tapez la longueur: "))
               larg=float(input("Tapez la largeur: "))
               G=GeomForm()
               S=G.rectangle(lon,larg)
               print(S)

           if i==1:
                rayon=float(input("Entrer le rayon: "))
                G=GeomForm()
                S=G.cercle(rayon)
                print(S)

           if i==2:
               coteA=float(input("Entrer le Cote A: "))
               coteB=float(input("Entrer le Cote B: "))
               coteC=float(input("Entrer le Cote C: "))
               G=GeomForm()
               S=G.triangle(coteA,coteB,coteC)
               print(S)


   except:
       print("Entrees invalides")



