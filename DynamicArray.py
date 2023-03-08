# -*- coding: utf-8 -*-
"""
author: MFWAMBA NDAYA (2GEI) AND KABAMBA MUTELA (2GC)

edited in  tuesday, November 10th
"""

import ctypes
class DynamicArray:
    """ A dynamic array class as a simplified Python list """
    def __init__(self):
        """Create an empty array."""
        self._n = 0 # count actual elements
        self._capacity = 1 # default array capacity
        self._A = self._make_array(self._capacity)
        # low-level array
    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n #retreive from array
    def __getitem__(self, k):
        """Return the item at position k"""
        if not 0 <= k < self._n:
            print('invalid index')
        return self._A[k] # retreive from array
    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity: 
            # not enough room
            self._resize(2*self._capacity)
            # so double capacity
        self._A[self._n] = obj
        self._n += 1
    def _resize(self, c):
        """Resize internal array to capacity c"""
        B= self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
    def _make_array(self,c):
        """Return new array with capacity c."""
        return (c*ctypes.py_object)()

if __name__ == '__main__':
    x= DynamicArray()
    print("Le tableau actuel possede {} elements et une capacite elementaire de {}".format(x._n, x._capacity))
    #On peut définir alors une nouvelle liste  de 30 elements
    for i in range(30):
       x.append(i)
    print("Ce nouveau tableau possède {} elements et une capacité de {}".format(len(x), x._capacity))
    # En se servant de __getitem__ on cherche la position d'un element dans notre tableau
    
    print("L'element qui occupe la position 15 est: {}".format(x.__getitem__(16)))
    
    # Puisque notre tableau possede 30 élément avec une capacité de 32
    # Dans ce cas si nous ajoutons 1'élément c'est seulement les nombres d'élément qui changer et non la capacité
    x.append(107)
    print("Le nombre d'élément du tableau est", x._n,"mais la capacité est toujours égale à", x._capacity )
    # Notre capacité devrait double si on ajoute deux autres elements
    x.append(0)
    x.append(5)
    print("Le nombre d'élément du tableau est", x._n,"Mais la capacité devient égale à", x._capacity )
    #Essayons avec un tableau ayant una capacité de 
    x._resize(35)
    print("Le nombre d'élément du tableau est {} et  la capacité devient égale à {}".format(x._n,x._capacity))
    #On crée un tableau avec une capacité quelconque
    y = x._make_array(10)
    print(y)
   
    
    
    
    
