#On peut aussi se servir du polymorphisme pour cette implementation


from math import *
from abc import ABC, abstractmethod

class GeomForm(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def surface(self):
        pass


"""creation  des classes """
#Nous definissons aussi pour chaque classe une methode 'mesures' pour recuperer la 
#surface et le perimetre

class Rectangle(GeomForm):
    def __init__(self, lon , larg):       
        self.__lon = lon
        self.__larg = larg
        self.__nom="rectangle"
    def perimeter(self):
        return 2*((self.__lon)+(self.__larg))
    def surface(self):
        return (self.__lon*self.__larg)
    def mesures(self):
        print("Le {} de {} sur {}  ".format(self.__nom,self.__larg,self.__lon))
        print("a un perimetre de {}".format(self.perimeter()))
        print("et une surface de {}".format(self.surface()))
class Cercle(GeomForm):
    def __init__(self, rayon : float):
        self.__rayon = rayon
        self.__nom="cercle"

    def perimeter(self):
        return pi*(self.__rayon)*2
    def surface(self):
        return pi*(self.__rayon)**2

    def mesures(self):
        print("Le {} de {} de rayon".format(self.__nom,self.__rayon))
        print("a un perimetre de {}".format(self.perimeter()))
        print("et une surface {}".format(self.surface()))

    
class Triangle(GeomForm):
    def __init__(self, coté1 : float, coté2 : float, coté3 : float):
        self.__coté1 = coté1
        self.__coté2 = coté2
        self.__coté3 = coté3
        self.__nom="Triangle"
    def perimeter(self):
        return self.__coté1 + self.__coté2 + self.__coté3
    def surface(self):
        d = (self.__coté1 + self.__coté2 + self.__coté3)/2
        return sqrt(d*(d-self.__coté1)*(d-self.__coté2)*(d-self.__coté3))
    def mesures(self):
        print("Le {} avec comme {}, {},{}, respectivement les mesures de trois cotes".format(self.__nom,self.__coté1,self.__coté2,self.__coté3))
        print("a un perimetre de {}".format(self.perimeter()))
        print("et une surface {}".format(self.surface()))

class Carre(Rectangle):
    def __init__(self, coté : float):
        
        Rectangle.__init__(self,coté,coté)
        self.__nom="carre"
        
class TriRectangle(Triangle):
    def __init__(self, base : float, hauteur : float):
        Triangle.__init__(self, base, hauteur, sqrt(base**2+hauteur**2)) 
        self.__nom="Triangle rectangle"

#Classe qui prend en charges les autres

class SurPerim: 
    def __init__(self, fiGeom : GeomForm):
        self.fiGeom = fiGeom

    def get_perimeter(self):
        return self.fiGeom.perimeter()

    def get_surface(self):
        return self.fiGeom.surface()  


