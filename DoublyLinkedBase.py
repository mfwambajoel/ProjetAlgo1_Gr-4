class _DoublyLinkedBase:
    """A base class providing a douby linked list representation"""

    class _Node:
        __slots__='_element','_prev','_next'

    def __init__(self,element,prev,next):
        self._element=element
        self._prev=prev
        self._next=next
    def __init__(self):
        """create an empty list"""
        self._header=self._Node(None,None,None)
        self._trailer=self._Node(None,None,None)
        self._trailer._prev=self._header
        self._size=0

    def __len__(self):
        """return the number of elements in the list"""
        return self._size

    def is_empty(self):
        returnself._size=0

    def _insert_between(self,e,predecessor,successor):
        """Add an  e element between two existing nodes"""
        newest=self._Node(e,predecessor,successor)
        predecessor._next=newest
        successor._prev=newest
        self._size +=1
        return newest

    def _delete_node(sel,node):
        """Delete non essential node"""
        predecessor=node._prev
        successor=node._next
        predecessor._next=next
        successor._prev=predecessor
        self._size -=1
        element=node._element
        node._prev=node._element=None
        return element
class LinkedDeque(_DoublyLinkedBase):
    def first(self):
        """return the element at the front of the deque"""

        if self.is_empty():
            raise Empty('Deque is empty')
        return self._header._next._element

    def last(self):
        """return the element at the back of the deque"""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element

    def insert_first(self,e):
        """Add an element to the front of the queue"""

        self._insert_between(e,self._header,self._header._next)

    def insert_last(self,e):
        """Add an element to the back of the deque"""
        self._insert_between(e,self._trailer._prev,self._trailer)
        
    def delete_first(self):
        """Remove and the return the element from the front of  Deque"""
        if is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        """remove and return the element from the back of deque"""
        if self.is_empty(self):
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)

LDeque=LinkedDeque()
L.insert_first(4)
print(L.__len__())