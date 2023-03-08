class LinkedStack:
    """LIFO stack implementation using a singly linked list for storage"""

    #------------------nested_Node class--------------

    class _Node:
        """Lighweight, nonpublic class for storing a singly linked node"""
        __slots__='_element','_next' #Rationaliser l'usage de la memoire

        def __init__(self,element,next): #initialise le champ des noeuds
            self._element=element       #reference a l'element utilisateur
            self._next=next              #reference au noeud siuvant
            
    #-----------------stack methods-------------------
    def __init__(self):
        """creation d'une pile vide"""
        self._head=None
        self._size=0

    def __len__(self):
        """Retourne le nombre d'elements dans la pile"""
        return self._size

    def is_empty(self):
        """Vrai si la pile est vide"""
        return self._size==0

    def push(self,e):
        """Ajouter l'element e au sommet de la liste"""
        self._head=self._Node(e,self._head) #creer et lier au nouveau noeud
        self._size +=1

    def top(self):
        """Retourne l'element au sommet de la liste"""
        if self.is_empty():
            raise Empty("stack is empty")
        return self._head._element

    def pop(self):
        """Supprime et retourne l'element depuis le sommet de laliste"""

        if self.is_empty():
            raise Empty('Stack is empty')
        answer=self._head._element
        self._head=self._head._next
        self._size -=1
        return answer

if __name__=='__main__':
    LStack=LinkedStack()
    LStack.push(4)
    LStack.push(4)
    LStack.pop()
    LStack.top()
    print(LStack.__len__())