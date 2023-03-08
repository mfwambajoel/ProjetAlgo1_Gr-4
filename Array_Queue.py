class ArrayQueue:
    """FIFO queue implementation using a Python lis as underlying storage"""
    DEFAULT_CAPACITY=10

    def __init__(self):
        """create an empty queue"""

        self._data=[None]*ArrayQueue.DEFAULT_CAPACITY
        self._size=0
        self._front=0

    def __len__(self):
        """return the number of elements in the queue"""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty"""

        return self._size==0

    def first(self):
        """Return the element at the front of the queue"""

        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue"""

        if self.is_empty():
            raise Empty('Queue is empty')
        answer=self._data[self._front]
        self._data[self._front]=None
        self._front=(self._front+1)%len(self._data)
        self._size -=1
        return answer

    def enqueue(self,e):
        """Add an element to the back of the queue"""
        if self._size==len(self._data):
            self._resize(2*len(self._data))
        avail=(self._front+self._size)%len(self._data)
        self._data[avail]=e
        self._size +=1

    def _resize(self,cap):
        """Resize to a new list of capacity"""

        old=self._dataself._data=[None]*cap
        walk=self._front
        for k in range(self._size):
            self._data[k]=old[walk]
            walk=(1+walk)%len(old)
        self._front=0

Arrqueue=ArrayQueue()
Arrqueue.enqueue(4)
Arrqueue.enqueue(7)
Arrqueue.enqueue(7)
Arrqueue.dequeue()
print(Arrqueue.__len__())
